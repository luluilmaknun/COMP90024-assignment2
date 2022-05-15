import { Component } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'analysis',
  templateUrl: './analysis.html',
  styleUrls: ['./analysis.css']
})
export class AnalysisComponent {
  public safeSrc: any;

  constructor(private sanitizer: DomSanitizer){}

  ngOnInit() {
    this.safeSrc = this.sanitizer.bypassSecurityTrustResourceUrl("http://localhost:3000/");
  }

}