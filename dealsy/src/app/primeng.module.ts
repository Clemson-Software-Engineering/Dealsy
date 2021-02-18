import { NgModule } from '@angular/core';

import {ButtonModule} from 'primeng/button';
import {InputTextModule} from 'primeng/inputtext';
import {TableModule} from 'primeng/table';

@NgModule({
  imports: [
    ButtonModule,
    InputTextModule,
    TableModule
  ],
  exports: [
    ButtonModule,
    InputTextModule,
    TableModule
  ]
})
export class PrimeNGModule {}