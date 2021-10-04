from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post
import re

# HTML Pages 
def home(request):
    allPosts = Post.objects.all().order_by('-sno')
    content = {'allPosts': allPosts}
    return render(request, 'home/home.html', content)
    
def about(request):
    return render(request, 'home/about.html')
    
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)

        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please Fill The Form Correctly and Submit Again!")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your Message Has Been Sent Successfully!")
        
    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query)>50:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count() == 0:
        messages.warning(request, "No search results found. Please check your query!")
    content = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', content)

# Authentication APIs 
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check the Errorneous Input
        # Usename should be 5 Charecters and Alphanumeric 
        if len(username) < 5 or not username.isalnum():
            messages.error(request, "Your Username must be minimum 5 characters and should be Alphanumeric Value!")
            return redirect('home')
        
        # Password should be match and Alphanumeric with special chatacter 
        if pass1 != pass2 or re.search('[0-9]', pass1) == None or re.search('[A-Z]', pass1) == None or re.search('[@_!#$%^&*()<>?/\|}{~:]', pass1) == None:
            messages.error(request, "Your Password doesn't match and should be atleast a Number, Uppercase and Special Chatacter")
            return redirect('home')
            
        # Create the User 
        myUser = User.objects.create_user(username, email, pass1)
        myUser.first_name = fname
        myUser.last_name = lname
        myUser.save()
        messages.success(request, "Your MyBlog Account has been created Successfully!")
        return redirect('home')
    else:
        return HttpResponse('404 -Not Found')   

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please try Again!")
            return redirect('home')
    return HttpResponse('404 -Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out!")
    return redirect('home')