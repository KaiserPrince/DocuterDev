from django.shortcuts import render, redirect
from .models import MyDataModel
from .models import SchoolDetailModel
from .forms import DataEntryForm
from .forms import SchoolDetailForm
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def export_pdf(request):
    data = MyDataModel.objects.all()  # Fetch your data
    html_template = render_to_string('data_export.html', {'data': data})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data_export.pdf"'
    weasyprint.HTML(string=html_template).write_pdf(response)
    return response

def school_data(request):
    if request.method == 'POST':
        form = SchoolDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poc:data-entry')  # Replace 'success' with the name of a success view
    else:
        form = SchoolDetailForm()
    return render(request, 'school_detail.html', {'form': form}) 

def data_entry(request):
    if request.method == 'POST':
        form = DataEntryForm(request.POST)
        if form.is_valid():
            form.save()
            form = DataEntryForm() # Create a new empty form
            return render(request, 'data_entry.html', {'form': form, 'success_message': 'Data saved successfully!'}) 
    else:
        form = DataEntryForm()
    return render(request, 'data_entry.html', {'form': form})

def list_data(request):
    data_list = MyDataModel.objects.all() 
    context = {'data_list': data_list}
    return render(request, 'data_list.html', context)

def export_question_paper_pdf(request):
    header = SchoolDetailModel.objects.get(id=1)
    data = MyDataModel.objects.all().values('question', 'option1', 'option2', 'option3', 'option4')  
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="question_paperq.pdf"'

    pdf_canvas = canvas.Canvas(response, pagesize=A4)

    # Title
    y_position = 800
    pdf_canvas.setFont('Times-Bold', 26)  
    pdf_canvas.drawString(200, y_position, header.school_name1) 
    
    y_position -= 15
    pdf_canvas.setFont('Times-Roman', 20)
    pdf_canvas.drawString(200, y_position, header.school_name2) 

    y_position -= 15
    pdf_canvas.setFont('Times-Roman', 16)
    pdf_canvas.drawString(200, y_position, header.school_address) 

    y_position -= 25
    pdf_canvas.setFont('Times-Bold', 18)
    pdf_canvas.drawString(200, y_position, 'Half Yearly Examination') 

    y_position -= 15
    pdf_canvas.setFont('Times-Bold', 18)
    pdf_canvas.drawString(15, y_position, '_______________________________________________________________') 
    
    # Questions and Options
    y_position -= 35  # Initial Y position for text
    pdf_canvas.setFont('Helvetica-Bold', 16) 
    pdf_canvas.drawString(30, y_position, 'I. Choose The Correct Answer:') 

    y_position -= 25  # Initial Y position for text
    for index, item in enumerate(data): 
        pdf_canvas.setFont('Helvetica', 16) 
        pdf_canvas.drawString(35, y_position, f"{index + 1}: {item.get('question', '')}")
        y_position -= 25  # Move down for the next question

        options = ['a', 'b', 'c', 'd'] 
        pdf_canvas.setFont('Helvetica', 14) 
        for option_label, option_text in zip(options, ['option1', 'option2', 'option3', 'option4']):
            pdf_canvas.drawString(40, y_position, f'{option_label}) {item.get(option_text, "")}')
            y_position -= 15  # Move down for the next option
        y_position -= 25  # Move down for the next question

    pdf_canvas.showPage()
    pdf_canvas.save()
    return response