import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FileUploadComponent } from './components/file-upload/file-upload.component';
import { FileDownloadComponent } from './components/file-download/file-download.component';
@Component({
  selector: 'app-root',
  imports: [FileUploadComponent , FileDownloadComponent , RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'quickdropfront';
}
