import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MilComponent } from './models/mil/mil.component';

const routes: Routes = [
  {path:'mil', component: MilComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
