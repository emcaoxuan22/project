# Generated by Django 2.2.5 on 2019-11-08 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CpuType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=30, verbose_name='Tên')),
            ],
        ),
        migrations.CreateModel(
            name='DiskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=30, verbose_name='Tên')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=30, verbose_name='Tên')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=100, verbose_name='Tên')),
                ('description', models.CharField(blank=True, max_length=500)),
                ('cpu', models.CharField(max_length=30)),
                ('ramSize', models.FloatField(verbose_name='Dung lượng RAM (GB)')),
                ('diskSize', models.FloatField(verbose_name='Dung lượng ổ cứng (GB)')),
                ('screenSize', models.FloatField(verbose_name='Kích thước màn hình (inch)')),
                ('weight', models.FloatField(verbose_name='Khối lượng (kg)')),
                ('price', models.IntegerField(verbose_name='Giá (₫)')),
                ('image', models.ImageField(upload_to='static/images', verbose_name='Ảnh sản phẩm')),
                ('cpuType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CpuType', verbose_name='Loại CPU')),
                ('diskType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.DiskType', verbose_name='Loại ổ cứng')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Manufacturer', verbose_name='Hãng sản xuất')),
            ],
        ),
    ]
