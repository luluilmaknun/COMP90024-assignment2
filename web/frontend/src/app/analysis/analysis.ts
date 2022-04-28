import { Component, OnInit } from '@angular/core';
import { AnalysisService } from './analysis.service';
import { Analysis } from './analysis.model';
import { ConnectableObservable } from 'rxjs';


@Component({
  selector: 'analysis',
  templateUrl: './analysis.html',
  styleUrls: ['./analysis.css']
})
export class AnalysisComponent implements OnInit {
  analysisRes: Analysis[] = [];

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
