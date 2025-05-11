import { CommonModule } from '@angular/common';
import { Component, input } from '@angular/core';
import { FileUploadService } from '../../services/file-upload.service';
import { response } from 'express';

@Component({
  selector: 'app-file-upload',
  imports: [CommonModule],
  templateUrl: './file-upload.component.html',
  styleUrl: './file-upload.component.scss'
})
export class FileUploadComponent {
  constructor(private fileUploadService: FileUploadService) {}
  selectfile: File | null = null;
  isDragging = false;
  downloadUrl: string = '';
  
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
  
  UploadFile(): void {
    if (!this.selectfile) return;
    this.fileUploadService.uploadFile(this.selectfile).subscribe(
      (response) => {
        console.log('Файл завантажено', response);
        if (response.download_url) {
          this.downloadUrl = response.download_url; // Збереження URL для завантаження
        }
      },
      (error) => {
        console.error('Помилка завантаження', error);
      }
    );
  }
  CopyLink(): void {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(this.downloadUrl).then(() => {
        console.log('Посилання скопійовано!');
        console.log(this.downloadUrl);
        alert('Посилання скопійовано в буфер обміну!');
      }).catch(err => {
        console.error('Не вдалося скопіювати', err);
        alert('Не вдалося скопіювати посилання');
      });
    } else {
      console.log('Clipboard API не підтримується в цьому браузері');
      alert('Clipboard API не підтримується в цьому браузері');
    }
  }
}
