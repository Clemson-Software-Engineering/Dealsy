import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Deal } from './data/interfaces/deal';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor(private http: HttpClient) {}

  async getDeals(term: string) {
    return this.http.get<any>('http://127.0.0.1:5000/deals/' + term)
        .toPromise()
        .then(res => <Deal[]>res)
        .then(res => { return res; });
  }

}
