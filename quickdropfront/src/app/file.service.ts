import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FileService {
  private apiUrl = '/api/files/';

  constructor(private http: HttpClient) { }

  getFiles(): Observable<any> {
    return this.http.get(this.apiUrl);
  }
}