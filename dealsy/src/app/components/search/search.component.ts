import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Table } from 'primeng/table';
import { SearchService } from 'src/app/services/search.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.sass']
})
export class SearchComponent implements OnInit {

  @ViewChild('dt') table: Table;

    deals: any[];

    loading: boolean = true;

    constructor(private searchService: SearchService, private route: ActivatedRoute) {}

    ngOnInit() {
      this.route.queryParams.subscribe(params => {
        this.searchService.getFakeDeals(params.query).then(deals => {
          this.deals = deals;
          this.loading = false;
        });
      });
    }

}
