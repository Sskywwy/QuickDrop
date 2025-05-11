import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class FileUploadService {
  private uploadUrl = 'http://127.0.0.1:8000/api/upload/';
  constructor(private http: HttpClient) {}
  uploadFile(file: File) {
    const formData = new FormData();
    formData.append('file', file);
    return this.http.post<{ download_url: string }>(this.uploadUrl, formData);
    };

}
  

