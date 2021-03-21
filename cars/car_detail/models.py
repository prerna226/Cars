from django.db import models

# Create your models here.

# This class is used for Car Brand
class CarBrand(models.Model):
    
    name= models.CharField(max_length=255,null=False)
    
    class Meta:
        db_table= 'car_brand'

# This class is used for Car Model
class CarModel(models.Model):
    
    name= models.CharField(max_length=255,null=False)
    brand_id= models.ForeignKey(CarBrand, db_column = 'brand_id',related_name='car_model_brand', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'car_model'

# This class is used for Car Varient
class CarVarient(models.Model):
    
    name= models.CharField(max_length=255,null=False)
    brand_id= models.ForeignKey(CarBrand, db_column = 'brand_id',related_name='car_var_brand', on_delete=models.CASCADE)
    model_id= models.ForeignKey(CarModel, db_column = 'model_id',related_name='car_var_model', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'car_varient'

# This class is used for Car Detail
class CarDetail(models.Model):
    
    brand_id= models.ForeignKey(CarBrand, db_column = 'brand_id',related_name='car_det_brand', on_delete=models.CASCADE)
    model_id= models.ForeignKey(CarModel, db_column = 'model_id',related_name='car_det_model', on_delete=models.CASCADE)
    varient_id= models.ForeignKey(CarVarient, db_column = 'varient_id',related_name='car_det_var', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'car_detail'