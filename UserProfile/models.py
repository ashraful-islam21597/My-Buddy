from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=120)
    contact=models.CharField(max_length=11)
    email=models.EmailField(max_length=120)
    username=models.CharField(max_length=120)
    password=models.CharField(max_length=120)
    confirmpassword = models.CharField(max_length=120)
    present_address=models.TextField(max_length=120,null=True,blank=True)
    permanent_address = models.TextField(max_length=120,null=True,blank=True)
    job = models.CharField(max_length=120,null=True,blank=True)
    profilepicture=models.ImageField(upload_to='profilepic')
    coverpicture = models.ImageField(upload_to='timelinecoverpic')
    def __str__(self):
        return self.username
    def profileimage(self):
        return self.profilepicture





class status(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    post=models.TextField(max_length=10000)
    caption=models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    timeline_pic = models.ImageField(upload_to='timelinepic')
    profile_pic = models.ImageField(upload_to='timelineprofilepic')
    cover_pic = models.ImageField(upload_to='timelinecoverpic')

    def img(self):
        return self.user.profilepicture

    def __str__(self):
        return self.user.name
    def np(self):
        return self.user.name
    def u(self):
        return self.user.username
    def time(self):
        date = (str(self.updated_at).split(' ')[0])
        d1 = date.split('-')
        d1_list = [int(i) for i in d1]
        m = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        f = (str(str(self.updated_at).split(' ')[1]).split(":")[0])
        g = (str(str(self.updated_at).split(' ')[1]).split(":")[1])
        k = int(f) + 6
        if k>=24:
            k1 = k - 24
            if k1 == 0:
                s = str(12) + (':') + g + " a.m "

            else:
                s = str(k1) + (':') + g + " a.m "

            return  s
        else:
            if k%12==0 :
                s = str(12) + (':') + g+" p.m"

            else:
                if k>12:
                    s = str(k%12) + (':') + g+" p.m "

                else:
                    s = str(k % 12) + (':') + g + " a.m "


            return s
    def date(self):
        date = (str(self.updated_at).split(' ')[0])
        d1 = date.split('-')
        d1_list = [int(i) for i in d1]
        m = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
        f = (str(str(self.updated_at).split(' ')[1]).split(":")[0])
        g = (str(str(self.updated_at).split(' ')[1]).split(":")[1])
        k = int(f) + 6
        if k>=24:
            s3=str(d1_list[2]+1)+","+str(m[d1_list[1]-1])+","+str(d1_list[0])
            k1 = k - 24
            if k1 == 0:
                s = str(12) + (':') + g + " a.m "

            else:
                s = str(k1) + (':') + g + " a.m "

                # s="am"

            return s3
        else:
            s3 = str(d1_list[2]) + "," + str(m[d1_list[1] - 1]) + "," + str(d1_list[0])
            if k%12==0 :
                s = str(12) + (':') + g+" p.m"
                print(s3,s)
            else:
                if k>12:
                    s = str(k%12) + (':')+g+"p.m"

                else:
                    s = str(k % 12) + (':') + g + " a.m "


            return s3
    def day(self):
        date = (str(self.updated_at).split(' ')[0])
        d1 = date.split('-')
        d1_list = [int(i) for i in d1]
        day=['Sat','Sun','Mon','Tue','Wed','Thu','Fri']
        m = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        f = (str(str(self.updated_at).split(' ')[1]).split(":")[0])
        g = (str(str(self.updated_at).split(' ')[1]).split(":")[1])
        k = int(f) + 6
        year=d1_list[0]
        sub=year-1900
        div=sub//4
        rem=sub%4
        b=[1,4,4,0,2,5,0,3,6,1,4,6] #144025036146

        if k>=24:

            total=(d1_list[2]+1)+sub+div+rem+b[d1_list[1] - 1]
            s4 = day[total % 7]

            return s4
        else:
            total = d1_list[2] + sub + div + rem + b[d1_list[1] - 1]
            s4 = day[total % 7]

            return s4
class friend(models.Model):
    user = models.ManyToManyField(Profile)
    username = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    contact = models.TextField(max_length=11)
    email = models.EmailField(max_length=120)
    def __str__(self):
        return self.name
class coverphotos(models.Model):

    userpic = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255, blank=True)
    cover_pic=models.ImageField(upload_to='photos/timelinecoverpic')
    uploaded_at = models.DateTimeField(auto_now_add=True)
class profilephotos(models.Model):

    userpic = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255, blank=True)
    profile_pic=models.ImageField(upload_to='photos/profilepic')
    uploaded_at = models.DateTimeField(auto_now_add=True)
class timelinephotos(models.Model):

    userpic = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255, blank=True)
    profile_pic=models.ImageField(upload_to='photos/timelinepic')
    uploaded_at = models.DateTimeField(auto_now_add=True)
class notification(models.Model):
    ins=models.CharField(max_length=120)
    message=models.CharField(max_length=120)
    fr=models.ForeignKey(Profile,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fr.name
    def massage(self):
        return self.message
    def time(self):
        return self.updated_at
class friendrequest(models.Model):
    instance = models.CharField(max_length=120)
    message = models.CharField(max_length=120)
    fr = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)









