import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Deal } from './data/interfaces/deal';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor(private http: HttpClient) {}

    async getFakeDeals(term: string) {
        return this.http.get<any>('../../assets/mock_deals.json')
            .toPromise()
            .then(res => <Deal[]>res)
            .then(res => res = res.filter(d => d.product.toLowerCase().includes(term.toLowerCase())))
            .then(res => { return res; });
    }
}
