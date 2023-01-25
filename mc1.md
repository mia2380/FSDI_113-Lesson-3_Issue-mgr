# Mini challenge 1

### Perform the initial set up of our new "task management system".

#### Steps:

1. Create a new django project within this folder; Make sure you name your configuration app `config`.
2. Create the following apps:
   2.1. pages
   2.2. accounts
   2.3. issues
3. Important: do not run migrations
4. Add the following models to issues/models.py
   4.1. Issue
   4.1.1. title
   4.1.2. summary
   4.1.3. description
   4.1.4. author - use get_user_model() to set your foreign key
   4.1.5. assignee - use get_user_model() to set your foreign key
   4.1.6. is_active - BooleanField
   4.1.7. created_on - Just like we defined for our Post model last class
   4.2. Status
   4.2.1. name
   4.2.2. description

#### Don't create a super user!
