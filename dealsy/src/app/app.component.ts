import { Component, ViewChild, ElementRef } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent {
  title = 'dealsy';

  @ViewChild('searchbar') searchbar: ElementRef;
  searchText = '';
  toggleSearch: boolean = false;

  constructor(private router: Router) {}

  openSearch() {
    this.toggleSearch = true;
    this.searchbar.nativeElement.focus();
  }
  searchClose() {
    this.searchText = '';
    this.toggleSearch = false;
  }

  searchDeals(term: string) {
    this.searchClose();
    if(term !== undefined && term !== '') {
      this.router.navigate(['search'], { queryParams: { query: term } });
    }
  }

}
