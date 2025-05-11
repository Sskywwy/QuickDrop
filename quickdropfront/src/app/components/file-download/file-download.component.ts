import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-file-download',
  imports: [],
  templateUrl: './file-download.component.html',
  styleUrl: './file-download.component.scss'
})
export class FileDownloadComponent {
  fileId!: number;
  fileName!: string;
  constructor(private route: ActivatedRoute) {}

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.fileId = params['id'];
      this.fileName = params['filename'];
    })
  }

  downloadFile(): void {
    const url = `http://127.0.0.1:8000/download/${this.fileId}/${this.fileName}`;
    window.open(url, '_blank');
  }
}
