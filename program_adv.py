import time

# وظيفة لعرض رسالة الترحيب
def welcome_message():
    print("مرحبًا بك في مغامرات في عالم البرمجة!")
    print("مهمتك هي تعلم أساسيات البرمجة وحل التحديات في كل مستوى.")
    print("لنبدأ المغامرة!\n")

# وظيفة لعرض التعليمات الأساسية
def show_instructions():
    print("التعليمات:")
    print("في كل مستوى، سيُطلب منك حل تحديات برمجية.")
    print("قم بكتابة الأوامر البرمجية الصحيحة لتتمكن من التقدم.\n")

# المستوى الأول: المتغيرات
def level_1():
    print("المستوى الأول: المتغيرات\n")
    print("في هذا المستوى، ستتعلم كيفية استخدام المتغيرات.\n")
    
    # تحدي
    attempts = 3
    while attempts > 0:
        print("التحدي: قم بتعريف متغير باسم 'name' واجعل قيمته 'Ahmed'.")
        answer = input("اكتب الحل: ").strip()
        if answer == "name = 'Ahmed'":
            print("أحسنت! لقد تجاوزت المستوى الأول بنجاح.\n")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"إجابة غير صحيحة. حاول مرة أخرى، لديك {attempts} محاولات.")
            else:
                print("للأسف، انتهت المحاولات. الحل الصحيح هو: name = 'Ahmed'")
                return False

# المستوى الثاني: الشروط
def level_2():
    print("المستوى الثاني: الشروط\n")
    print("في هذا المستوى، ستتعلم كيفية استخدام العبارات الشرطية.\n")
    
    # تحدي
    attempts = 3
    while attempts > 0:
        print("التحدي: قم بكتابة عبارة شرطية تتحقق إذا كانت قيمة المتغير x أكبر من 10.")
        answer = input("اكتب الحل: ").strip()
        if answer == "if x > 10:":
            print("رائع! لقد تجاوزت المستوى الثاني بنجاح.\n")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"إجابة غير صحيحة. حاول مرة أخرى، لديك {attempts} محاولات.")
            else:
                print("للأسف، انتهت المحاولات. الحل الصحيح هو: if x > 10:")
                return False

# المستوى الثالث: الحلقات
def level_3():
    print("المستوى الثالث: الحلقات\n")
    print("في هذا المستوى، ستتعلم كيفية استخدام الحلقات.\n")
    
    # تحدي
    attempts = 3
    while attempts > 0:
        print("التحدي: قم بكتابة حلقة for تقوم بطباعة الأرقام من 1 إلى 5.")
        answer = input("اكتب الحل: ").strip()
        if answer == "for i in range(1, 6):\n print(i)":
            print("مذهل! لقد تجاوزت المستوى الثالث بنجاح.\n")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"إجابة غير صحيحة. حاول مرة أخرى، لديك {attempts} محاولات.")
            else:
                print("للأسف، انتهت المحاولات. الحل الصحيح هو:\nfor i in range(1, 6):\n print(i)")
                return False

# المستوى الرابع: الدوال
def level_4():
    print("المستوى الرابع: الدوال\n")
    print("في هذا المستوى، ستتعلم كيفية تعريف واستخدام الدوال.\n")
    
    # تحدي
    attempts = 3
    while attempts > 0:
        print("التحدي: قم بتعريف دالة باسم 'greet' تقوم بطباعة 'Hello'.")
        answer = input("اكتب الحل: ").strip()
        if answer == "def greet():\n print('Hello')":
            print("أحسنت! لقد تجاوزت المستوى الرابع بنجاح.\n")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"إجابة غير صحيحة. حاول مرة أخرى، لديك {attempts} محاولات.")
            else:
                print("للأسف، انتهت المحاولات. الحل الصحيح هو:\ndef greet():\n print('Hello')")
                return False

# المستوى الخامس: المشروع النهائي
def final_level():
    print("المستوى الخامس: المشروع النهائي\n")
    print("الآن حان الوقت لتطبيق ما تعلمته في مشروع صغير.\n")
    
    # تحدي
    attempts = 3
    while attempts > 0:
        print("المهمة: قم بكتابة برنامج بسيط يسأل المستخدم عن اسمه ويقوم بتحيته.")
        answer = input("اكتب الحل: ").strip()
        if answer == "name = input('ما اسمك؟ ')\nprint(f'مرحبًا، {{name}}!')":
            print("مذهل! لقد أنهيت المغامرة بنجاح!")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"إجابة غير صحيحة. حاول مرة أخرى، لديك {attempts} محاولات.")
            else:
                print("للأسف، انتهت المحاولات. الحل الصحيح هو:\nname = input('ما اسمك؟ ')\nprint(f'مرحبًا، {{name}}!')")
                return False

# الوظيفة الرئيسية التي تدير اللعبة
def main():
    welcome_message()
    show_instructions()

    # الانتقال بين المستويات
    if level_1():
        if level_2():
            if level_3():
                if level_4():
                    final_level()

# استدعاء الوظيفة الرئيسية لتشغيل البرنامج
if __name__ == "__main__":
    main()
