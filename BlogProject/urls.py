
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



from myadmin import views


urlpatterns = [
     # Home page
   
    # Demo page


    

    path('', views.home, name='home'),
    # View a specific blog post
    path('blogview/<int:id>', views.blogview ,name='blogview'),
    # Admin dashboard
    path('admin/', views.admin,name='admin'),
    path('admin/login/', views.admin_login, name='admin_login'),
    # Verify
    # path('verify', views.verify, name='verify'),
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    # Category section
    path('add-category', views.category),
    path('storecategory', views.storecat),
    path('view-category', views.view_category),
    path('editcat/<int:id>', views.editcat, name='editcat'),
    path('updatecat/<int:id>', views.updatecat, name='updatecat'),
    path('deletecat/<int:id>', views.deletecat, name='deletecat'),
    # Subcategory section
    path('add-subcategory', views.subcategory),
    path('storesubcategory', views.storesubcat),
    path('view-subcategory', views.view_subcategory),
    path('editsubcat/<int:id>', views.editsubcat, name='editsubcat'),
    path('updatesubcat/<int:id>', views.updatesubcat, name='updatesubcat'),
    path('deletesubcat/<int:id>', views.deletesubcat, name='deletesubcat'),
    # Add a new blog post
    path('add-post', views.post),
    path('storeblog', views.storeblog),
    # View all blog posts
    path('view-blog', views.view_post),
    path('view-post/', views.view_post, name='view-post'),
    # Edit a blog post
    # path('editblog/<int:id>', views.editblog, name='editblog'),
    path('edit-blog/<int:id>/',views.editblog, name='edit-blog'),
  
    path('updatepost/<int:id>', views.updatepost, name='updatepost'),
   
    # Delete a blog post
    path('delete-blog/<int:id>/', views.delete_blog, name='delete-blog'),
   
    
   
    
    path('singlepost/<int:post_id>/', views.singlepost, name='singlepost'),
    # path('post/<int:pk>/', views.singlepost, name='singlepost'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('search/', views.search_view, name='search'),
    # path('search_blogs/', views.search_blogs, name='search_blogs'),
    path('search/', views.search_blogs, name='search-view'),
    path('base/', views.base, name='base'),
    # path('contact/', views.submit_contact, name='submit_contact'),
    path('contact/', views.contact, name='contact'),
    
    path('view-contact/', views.view_contact, name='view_contact'),
    
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('blog/', views.blog_page, name='blog_page'),
   
    


    path('subscribes/', views.subscribes, name='subscribe'),






    path('signup/', views.student_signup, name='student_signup'),
    path('login/', views.student_login, name='student_login'),
    path('logout/', views.student_logout, name='student_logout'),
    
   
    path('dashboards/', views.student_dashboard, name='student_dashboard'),
    path('ebooks/', views.ebook_listing, name='ebook_listing'),
    path('buy/<int:ebook_id>/', views.buy_ebook, name='buy_ebook'),
    path('download-pdf/<int:ebook_id>/', views.download_pdf, name='download_pdf'),

    path('add-ebook/', views.add_ebook, name='add_ebook'),
    path('view_ebook/', views.view_ebook, name='view_ebook'),
    path('update_ebook/<int:ebook_id>/', views.update_ebook, name='update_ebook'),
    path('delete_ebook/<int:ebook_id>/', views.delete_ebook, name='delete_ebook'),
   
]
   


    
   
   


if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
        urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

