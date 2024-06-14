from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib import messages #import messages
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from myadmin.forms import CategoryForm,SubcategoryForm,BlogForm
from myadmin.models import Category,Subcategory,Blog
from myadmin.   forms import Category as Category
from myadmin.   forms import Subcategory as Subcategory
from .models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SearchForm
from django.db.models import Q
from .forms import ContactForm
from .models import Contact


from django.http import JsonResponse



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
def admin(request):
    return render(request,'login.html')


# def verify(request):
#     msg=''
#     if request.method == "POST":
#         name = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=name,password=password)
#         if user is not None:
#             login(request, user)
#             request.session['name']=user.username
#             #request.session['adminLogin']=True
#             messages.error(request, 'Welcome to Admin Panel..!')
#             return redirect("/dashboard")
#         else:
#             messages.error(request, 'username or password not correct')
#             return render(request,'login.html')
#     else:
#         return render(request,'login.html')


# Dashboard
def dashboard(request):
    # name=request.session.get('name','')
    messages.success(request,"Created Dashboard....")
    return render(request,'dashboard.html')


#category 
def category(request):
  return render(request,'category.html')


def storecat(request):
    if request.method == "POST":
        name = request.POST.get('category_name')
        if Category.objects.filter(category_name=name):
            messages.success(request, "Category name is already taken in Category Table .....Please Enter another Name Thankyou!" )
            return redirect("/add-category")
        else:
            form = CategoryForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Category Insert Successfully." )
                return redirect("/view-category",{'form':form})
    else:
        form= CategoryForm()
    return render(request,'category.html',{'form':form})



#category  view
def view_category(request):
    category_views = Category.objects.all()
    return render(request, 'view-category.html', {'categoryviews': category_views})
def editcat(request,id):
    categoryview=Category.objects.get(id=id)
    return render(request,'editcategory.html',{'categoryview':categoryview})

def updatecat(request,id):
    categoryview=Category.objects.get(id=id)
    if request.method == "POST":
        form= CategoryForm(request.POST,request.FILES,instance=categoryview)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Form Updated Successfully." )
            return redirect("/view-category")
        else:
            form=CategoryForm()
            messages.success(request, "Category Form is Not Updated Pls Try Again..." )
        return render(request,'editcategory.html',{'form':form,'categoryview':categoryview})

def deletecat(request,id):
    categoryview=Category.objects.get(id=id)
    categoryview.delete()
    messages.success(request, "Category Form Record Delete are Successfully." )
    return redirect("/view-category")
 



#------------------------------------------Subcategory -------------------------------
def subcategory(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subcategory')
    else:
        form = SubcategoryForm()
    categoryview = Category.objects.all()
    subcategories = Subcategory.objects.all()
    return render(request, 'subcategory.html', {'form': form, 'categoryviews': categoryview, 'subcategories': subcategories})


def storesubcat(request):
    if request.method == "POST":
        name = request.POST.get('subcategory_name')  # Potential cause of KeyError
        if Subcategory.objects.filter(subcategory_name=name):
            messages.success(request, "SubCategory name is already taken in Category Table .....Please Enter another Name Thankyou!" )
            return redirect("/add-subcategory")
        else:
            form = SubcategoryForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Subcategory Insert Successfully." )
                return redirect("/view-subcategory",{'form':form})
    else:
        form= SubcategoryForm()
    return render(request,'subcategory.html',{'form':form})
#subcategory  view
def view_subcategory(request):
    subcategoryview = Subcategory.objects.all()
    return render(request, 'view-subcategory.html', {'subcategoryview': subcategoryview})


    
def editsubcat(request,id):
    categoryview=Category.objects.all()
    subcategoryview=Subcategory.objects.get(id=id)
    return render(request,'editsubcategory.html',{'categoryviews':categoryview,'subcategoryview':subcategoryview})

def updatesubcat(request,id):
    subcategoryview=Subcategory.objects.get(id=id)
    if request.method == "POST":
        form= SubcategoryForm(request.POST,request.FILES,instance=subcategoryview)
        if form.is_valid():
            form.save()
            messages.success(request, "Subctegory Form Updated Successfully." )
            return redirect("/view-subcategory")
        else:
            form=SubcategoryForm()
            messages.success(request, "Subcategory Form is Not Updated Pls Try Again..." )
        return render(request,'editsubcategory.html',{'form':form,'subcategoryview':subcategoryview})

def deletesubcat(request,id):
    subcategoryview=Subcategory.objects.get(id=id)
    subcategoryview.delete()
    messages.success(request, "Subcategory Form Record Delete are Successfully." )
    return redirect("/view-subcategory")
 

#post 
def post(request):
    # Retrieve all categories and subcategories from the database
    categoryview = Category.objects.all()
    subcategoryview = Subcategory.objects.all()
    
    # Render the post.html template with the retrieved categories and subcategories
    return render(request, 'post.html', {'categoryviews': categoryview, 'subcategoryviews': subcategoryview})
def storeblog(request):
    if request.method == "POST":
        # Retrieve the post_name from the form data
        name = request.POST.get('post_name')
        # Check if a blog post with the same name already exists in the database
        if Blog.objects.filter(post_name=name):
            # If a blog post with the same name exists, display a message to the user
            messages.success(request, "Post name is already taken in Category Table. Please enter another name. Thank you!")
            return redirect("/add-post")  # Redirect to the add-post URL or any suitable URL
        else:
            # If the post name is unique, proceed with form validation and saving
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Blog inserted successfully.")
                return redirect("/view-blog")  # Redirect to the view-blog URL or any suitable URL
    else:
        # If the request method is not POST, create a new instance of the BlogForm
        form = BlogForm()
    return render(request, 'post.html', {'form': form})


def view_post(request):
    # Retrieve all blog posts from the database
    blogview = Blog.objects.all()

    
    # Render the view-post.html template with all blog posts
    return render(request, 'view-post.html', {'blogview': blogview})
def blogview(request, id):
    # Retrieve the specific blog post with the given ID or return a 404 error if it doesn't exist
    blogview = get_object_or_404(Blog, id=id)
    
    
    # Fetch all blog posts to be displayed in the sidebar or any other related section
    blogviews = Blog.objects.all()
    
    # Render the singlepost.html template with the specific blog post and all blog posts
    return render(request, 'singlepost.html', {'blogview': blogview, 'blogviews': blogviews})

# ediblog
def editblog(request, id):
    try:
        # Fetch all categories and subcategories from the database
        categoryview = Category.objects.all()
        subcategoryview = Subcategory.objects.all()

        # Retrieve the blog post with the given ID
        blogviewedit = Blog.objects.get(id=id)

    except Blog.DoesNotExist:
        # Handle the case where the blog with the given id doesn't exist
        return HttpResponse("Blog does not exist")

    # Render the editpost.html template with the retrieved categories, subcategories, and blog post
    return render(request, 'editpost.html', {'categoryviews': categoryview, 'subcategoryviews': subcategoryview, 'blogviewedit': blogviewedit})
def updatepost(request, id):
    try:
        # Retrieve the blog post with the specified ID or return a 404 error
        blogviewedit = get_object_or_404(Blog, id=id)
        
        if request.method == "POST":
            # Populate the form with the POST data and files, using the retrieved blog post as the instance
            form = BlogForm(request.POST, request.FILES, instance=blogviewedit)
            if form.is_valid():
                # Save the form if it is valid
                form.save()
                messages.success(request, "Blog Form Updated Successfully.")
                return redirect("view-post")  # Redirect to the view-post URL after successful update
            else:
                messages.error(request, "Blog Form is Not Updated. Please Try Again...")
        else:
            # If it's a GET request, populate the form with the data from the retrieved blog post
            form = BlogForm(instance=blogviewedit)
        
        # Render the editpost.html template with the form and the retrieved blog post
        return render(request, 'editpost.html', {'form': form, 'blogviewedit': blogviewedit})
    
    except Blog.DoesNotExist:
        # Handle case where the blog post with the specified ID does not exist
        messages.error(request, "Blog post does not exist.")
        return redirect("view-post")  # Redirect to a suitable page or URL
    except Exception as e:
        # Handle any other unexpected errors
        messages.error(request, f"An error occurred: {e}")
        return redirect("view-post")  # Redirect to a suitable page or URL
# delete  post 
def delete_blog(request, id):
    try:
        # Attempt to retrieve the blog post with the given ID
        post = get_object_or_404(Blog, id=id)
        # Delete the retrieved blog post
        post.delete()
        # Display a success message if deletion is successful
        messages.success(request, "Blog post deleted successfully.")
    except Blog.DoesNotExist:
        # Handle the case where the blog post with the given ID does not exist
        messages.error(request, "Blog post does not exist.")
    except Exception as e:
        # Handle any other unexpected errors
        messages.error(request, f"An error occurred: {e}")
    
    # Redirect the user to the view-post URL after deletion
    return redirect("view-post")

#Slider 


# demo

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blog, Category

def home(request):
    # Retrieve all blog posts from the database
    
    blogview = Blog.objects.all()
    
    # Pagination
    paginator = Paginator(blogview, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Retrieve categories
    categoryview = Category.objects.all()
    
    # Other data
    popular_post = Blog.objects.filter(section='Popular', status=1).order_by('-id')[:4]
    recent_post = Blog.objects.filter(section='Recent', status=1).order_by('-id')[:4]
    main_post = Blog.objects.filter(main_post=True).first()
    editor_pick = Blog.objects.filter(section='Editor_Pick', status=1).order_by('-id')
    trending = Blog.objects.filter(section='Trending', status=1).order_by('-id')
    inspiration = Blog.objects.filter(section='Inspiration', status=1).order_by('-id')[:2]
    latest_posts = Blog.objects.filter(section='Latest_Posts', status=1).order_by('-id')[:4]

    context = {
        'popular_post': popular_post,
        'recent_post': recent_post,
        'main_post': main_post,
        'editor_pick': editor_pick,
        'trending': trending,
        'inspiration': inspiration,
        'latest_posts': latest_posts,
        'categoryview': categoryview,
        'blogview': page_obj,  # Pass paginated queryset to template
    }

    # Render the template with the context
    return render(request, 'index2.html', context)


def singlepost(request, post_id):
    # Retrieve the specific blog post based on the provided post_id
    blog = get_object_or_404(Blog, id=post_id)
    
    # Retrieve all blog posts (optional)
    blog_list = Blog.objects.all()
    
    # Retrieve related posts
    popular_post = Blog.objects.filter(section='Popular', status=1).order_by('-id')[:4]
    recent_post = Blog.objects.filter(section='Recent', status=1).order_by('-id')[:4]
    main_post = Blog.objects.filter(main_post=True).first()
    editor_pick = Blog.objects.filter(section='Editor_Pick', status=1).order_by('-id')
    trending = Blog.objects.filter(section='Trending', status=1).order_by('-id')
    inspiration = Blog.objects.filter(section='Inspiration', status=1).order_by('-id')[:2]
    latest_posts = Blog.objects.filter(section='Latest_Posts', status=1).order_by('-id')[:4]

    context = {
        'popular_post': popular_post,
        'recent_post': recent_post,
        'main_post': main_post,
        'editor_pick': editor_pick,
        'trending': trending,
        'inspiration': inspiration,
        'latest_posts': latest_posts,
        'blog': blog,  # Pass the specific blog post instance
        'blog_list': blog_list,  # Pass all blog posts (optional)
    }
    
    # Render the singlepost.html template with the specific blog post and all blog posts
    return render(request, 'singlepost.html', context)



def search_blogs(request):
    search_query = request.POST.get('search_query', '')  # Use get() method with a default value
    if len(search_query) > 50:
        allpost = []
    else:
        allpost = Blog.objects.filter(
            Q(post_title__icontains=search_query) |  # Search in the post title
            Q(category_id__icontains=search_query) |  # Search in the category ID
            Q(subcategory_id__icontains=search_query) |  # Search in the subcategory ID
            Q(details__icontains=search_query) |  # Search in the details
            Q(author__icontains=search_query) |  # Search in the author
            Q(section__icontains=search_query)  # Search in the section
        )

        if allpost.count() == 0:

         messages.error(request, "No search results found")

    pra = {'allpost': allpost, 'search_query': search_query}
    return render(request, 'search.html', pra)

def base(request):
    return render(request, 'base.html')
   





 
def view_contact(request):
    contacts = Contact.objects.all()
    return render(request, 'view_contact.html', {'contacts': contacts})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')  # Replace 'success.html' with your success template
    else:
        form = ContactForm()
    return render(request, 'Contact.html', {'form': form})

def delete_contact(request, contact_id):
    # Get the contact object from the database
    contact = get_object_or_404(Contact, pk=contact_id)
    
    # Delete the contact
    contact.delete()
    
    # Redirect to a success page or any other appropriate page
    return redirect('view_contact')  # Assuming 'view_contacts' is the name of the view that displays all contacts




def blog_page(request):
    blogviews = Blog.objects.all()
    
    # Pagination
    paginator = Paginator(blogviews, 6)  # Change '6' to the desired number of posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog.html', {'blogview': page_obj})



from django.core.mail import send_mail
from .forms import SubscriptionForm

def subscribes(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Save the email address to database (if using a model)
            # subscriber = Subscriber(email=email)
            # subscriber.save()

            # Send confirmation email (optional)
            # send_mail('Subscription Confirmation', 'You have subscribed successfully.', 'from@example.com', [email])

            # Redirect to a thank you page or show a success message
            return render(request, 'thank_you.html')
    else:
        form = SubscriptionForm()
    return render(request, 'subscribe.html', {'form': form})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ebook
from .forms import EbookForm
import stripe
from django.conf import settings

def student_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('student_login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if not user.is_staff:  # Ensure this is a regular user
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'You are not authorized to access student dashboard.')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Missing username or password.')
    return render(request, 'auth/login.html')

@login_required
def student_logout(request):
    logout(request)
    return redirect('home')

def admin_login(request):
    if request.method == "POST":
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_staff:  # Check if the user is an admin
                    login(request, user)
                    request.session['name'] = user.username
                    messages.success(request, 'Welcome to Admin Panel..!')
                    return redirect("/dashboard")
                else:
                    messages.error(request, 'You are not authorized to access admin panel.')
            else:
                messages.error(request, 'Username or password not correct.')
    return render(request, 'login.html')

@login_required
def ebook_listing(request):
    ebooks = Ebook.objects.all()
    return render(request, 'auth/ebook_listing.html', {'ebooks': ebooks})

def view_ebook(request):
    ebooks = Ebook.objects.all()
    return render(request, 'auth/view_ebook.html', {'ebooks': ebooks})

@login_required
def add_ebook(request):
    ebook = None
    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES)
        if form.is_valid():
            ebook = form.save()
            messages.success(request, 'Ebook added successfully.')
            return redirect('view_ebook')
            # No need to redirect here, just pass the ebook to the template context
    else:
        form = EbookForm()
    return render(request, 'auth/add_ebook.html', {'form': form, 'ebook': ebook})

@login_required
def update_ebook(request, ebook_id):
    ebook = get_object_or_404(Ebook, id=ebook_id)
    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES, instance=ebook)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ebook updated successfully.')
            return redirect('view_ebook')
    else:
        form = EbookForm(instance=ebook)
    return render(request, 'auth/update_ebook.html', {'form': form})

@login_required
def delete_ebook(request, ebook_id):
    ebook = get_object_or_404(Ebook, id=ebook_id)
    if request.method == 'POST':
        ebook.delete()
        messages.success(request, 'Ebook deleted successfully.')
        return redirect('ebook_listing')
    return render(request, 'auth/ebook_listing.html')



@login_required
def buy_ebook(request, ebook_id):
    ebook = get_object_or_404(Ebook, pk=ebook_id)
    password_correct = False
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == 'love':  # Replace 'love' with your actual password
            password_correct = True
        else:
            messages.error(request, 'Incorrect password. Please try again.')
    return render(request, 'auth/buy_ebook.html', {'ebook': ebook, 'password_correct': password_correct})

from django.contrib.auth.models import User
@login_required
def student_dashboard(request):
    ebooks = request.user.purchased_ebooks.all()
    total_books = Ebook.objects.count()
    total_users = User.objects.count()
    total_downloads = sum(ebook.download_count for ebook in Ebook.objects.all())
    return render(request, 'auth/dashboards.html', {
        'ebooks': ebooks,
        'total_books': total_books,
        'total_users': total_users,
        'total_downloads': total_downloads
    })
import os

def download_pdf(request, ebook_id):
    ebook = Ebook.objects.get(id=ebook_id)
    pdf_file_path = os.path.join(settings.MEDIA_ROOT, ebook.file.name)
    with open(pdf_file_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(ebook.file.name)
        return response


