from django.contrib import admin
from .models import Students,Classroom
from firebase_admin import firestore


@admin.register(Students)
class StudentModelAdmin(admin.ModelAdmin):
    """
    Admin class for managing Students model.
    """
    db = firestore.client()

    def save_model(self, request, obj, form, change):
        """
        Override save_model method to perform CRUD operations on Firebase Firestore.
        
        If the request method is POST, add a new document to Firestore.
        If the request method is PUT, update an existing document in Firestore.
        """

        try:
            main_collection_data = {
                'name': obj.name,
                'age': obj.age
            }

            child_collection_data = {
                'name': obj.classroom.name
            }

            parent_ref = self.db.collection('students').document(str(obj.id))
            child_ref = parent_ref.collection('classroom').document(str(obj.classroom.id))

            if request.method == 'POST':
                # Create a new document in Firestore
                parent_ref.set(main_collection_data)
                if obj.classroom:
                    child_ref.set(child_collection_data)

            elif request.method == 'PUT':
                if obj.id:
                    # Update the corresponding document in Firestore
                    parent_ref.update(main_collection_data)
                    if obj.classroom.id:
                        child_ref.update(child_collection_data)

            # Call the original save_model method to save the model object in Django
            super().save_model(request, obj, form, change)
        
        except Exception as e:
            # Handle the exception or display an error message
            print(f"An error occurred: {str(e)}")

    def delete_model(self, request, obj):
        """
        Override delete_model method to delete the corresponding document from Firestore.
        """

        if obj.id:
            doc_ref = self.db.collection('students').document(str(obj.id))
            doc_ref.delete()

        # Call the original delete_model method to delete the model object in Django
        super().delete_model(request, obj)


admin.site.register(Classroom)

