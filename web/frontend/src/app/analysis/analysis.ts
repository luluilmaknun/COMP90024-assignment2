import { Component, OnInit } from '@angular/core';
import { AnalysisService } from './analysis.service';


@Component({
  selector: 'analysis',
  templateUrl: './analysis.html',
  styleUrls: ['./analysis.css']
})
export class AnalysisComponent implements OnInit {
  analysisRes: any = {};

  constructor(private analysisApi: AnalysisService) {
  }

  ngOnInit() {
    this.analysisApi.getAnalysis()
      .subscribe({
        next: (res) => {
          console.log(res);
          this.analysisRes = res;
        },
        error: (err) => console.log(err),
      });
  }
}
