import { Component, OnInit } from '@angular/core';
import {Teste } from './metodo'; 

import {MilService} from '../../service/mil.service';

@Component({
  selector: 'app-mil',
  templateUrl: './mil.component.html',
  styleUrls: ['./mil.component.css']
})


export class MilComponent implements OnInit {
  ss: Teste;
  mil={"0":"", "1":"", "2":"", "3":"", "4":"", "5":"", "6":""};
  teste=[]
  metodo: {};
  message =[]
  constructor(private milService: MilService) { }

  ngOnInit() {
  this.metodo={}
  console.log(this.message)
  }
  onClick(t: any){

    console.log(t)
    this.milService.onCalcular(this.metodo).subscribe(resposta =>{
      this.message = resposta;
      console.log(resposta)
    }) 
  }


  
}



