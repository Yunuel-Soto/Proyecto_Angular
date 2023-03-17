import { Component } from '@angular/core';
import { UserInsertService } from './user-insert.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'presentacion';
  nick_name = '';
  fullname = '';
  
  constructor(private userInsertService: UserInsertService) {}

  public onSubmit() {
    const formData = new FormData();
    formData.append('nick_name', this.nick_name);

    this.userInsertService.postFormData(formData).subscribe(
      error => {console.log(error)},
      success => {console.log(success)}
    );
  }
}