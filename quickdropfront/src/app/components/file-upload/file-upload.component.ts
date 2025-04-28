import { CommonModule } from '@angular/common';
import { Component, input } from '@angular/core';

@Component({
  selector: 'app-file-upload',
  imports: [CommonModule],
  templateUrl: './file-upload.component.html',
  styleUrl: './file-upload.component.scss'
})
export class FileUploadComponent {
  selectfile: File | null = null;
  isDragging = false;
  
  onDragEnter(event: DragEvent): void {
    event.preventDefault();
    this.isDragging = true;
  }
  onDragOver(event: DragEvent): void {
    event.preventDefault();
    this.isDragging = true;

  }

  clearFileInput(): void {
    this.selectfile = null;
  }
  onDragLeave (event: DragEvent) {
    event.preventDefault()
    this.isDragging = false
  }

  onDrop (event: DragEvent) {
    event.preventDefault()
    console.log('➡️ onDragEnter', event);
    this.isDragging = false

    if (event.dataTransfer?.files.length) {
      this.selectfile = event.dataTransfer.files[0];
      console.log("Файл Вибраний: ", this.selectfile);
    }
  }
  onFileSelected(event: Event): void {
    const input= event.target as HTMLInputElement;
    if (input.files && input.files.length) {
      this.selectfile = input.files[0];
      console.log("Файл Вибраний: ", this.selectfile);
  
    }
  }

  triggerFileInput(): void {
    const fileinput = document.getElementById('file-upload') as HTMLInputElement;
    fileinput.click();
  }
}
