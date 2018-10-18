import {Page} from '@/models/page'
import ajax from './ajax'

export class PageApi {
  static requestPage (pageIdx) {
    return ajax.get(`post/${pageIdx}/`)
  }
}
