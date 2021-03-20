import { NgModule } from '@angular/core';

import {ButtonModule} from 'primeng/button';
import {InputTextModule} from 'primeng/inputtext';
import {TableModule} from 'primeng/table';
import {RatingModule} from 'primeng/rating';

@NgModule({
  imports: [
    ButtonModule,
    InputTextModule,
    TableModule,
    RatingModule
  ],
  exports: [
    ButtonModule,
    InputTextModule,
    TableModule,
    RatingModule
  ]
})
export class PrimeNGModule {}