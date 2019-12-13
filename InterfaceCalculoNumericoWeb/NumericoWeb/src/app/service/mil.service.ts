import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MilService {

 private milUrl = 'http:
 //127.0.0.1:5000/interativo';

  constructor(private http: HttpClient) { }

    onCalcular(t: any){
     return this.http.post(this.milUrl, t)
  }
}
