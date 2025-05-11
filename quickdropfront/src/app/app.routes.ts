import { Routes } from '@angular/router';
import { FileDownloadComponent } from './components/file-download/file-download.component';
import { FileUploadComponent } from './components/file-upload/file-upload.component';

export const routes: Routes = [
    {path: '', component: FileUploadComponent},
    {path: 'download/:id/:filename', component: FileDownloadComponent}
];
