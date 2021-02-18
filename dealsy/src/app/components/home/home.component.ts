import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.sass']
})
export class HomeComponent implements OnInit {

  searchTerm: string;

  constructor(private router: Router) {}

  ngOnInit(): void {}

  searchDeals() {
    if(this.searchTerm !== undefined && this.searchTerm !== '') {
      this.router.navigate(['search'], { queryParams: { query: this.searchTerm } });
    }
  }

}
