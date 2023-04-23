DROP TABLE IF EXISTS pu_supplier_eval;

CREATE TABLE pu_supplier_eval (
  supplier_eval_id int8 NOT NULL PRIMARY KEY  ,
  eval_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP  ,
  quater char(1) NOT NULL DEFAULT 1  ,
  supplier_name varchar(50) NOT NULL  ,
  product varchar(50) NOT NULL  ,
  amt numeric(16, 2) NOT NULL DEFAULT 0  ,
  eval_dept varchar(20) NOT NULL  ,
  price_score numeric(16) NOT NULL DEFAULT 0  ,
  service_stat_score numeric(16) NOT NULL DEFAULT 0  ,
  product_qual_score numeric(16) NOT NULL DEFAULT 0  ,
  after_sale_score numeric(16) NOT NULL DEFAULT 0  ,
  creator_id int8 NOT NULL DEFAULT 1  ,
  create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP  

);

COMMENT ON COLUMN public.pu_supplier_eval.supplier_eval_id IS '主键';
COMMENT ON COLUMN public.pu_supplier_eval.eval_date IS '考评时间';
COMMENT ON COLUMN public.pu_supplier_eval.quater IS '季度';
COMMENT ON COLUMN public.pu_supplier_eval.supplier_name IS '供应商名称';
COMMENT ON COLUMN public.pu_supplier_eval.product IS '采购产品';
COMMENT ON COLUMN public.pu_supplier_eval.amt IS '采购金额';
COMMENT ON COLUMN public.pu_supplier_eval.eval_dept IS '相关考评部门';
COMMENT ON COLUMN public.pu_supplier_eval.price_score IS '价格';
COMMENT ON COLUMN public.pu_supplier_eval.service_stat_score IS '服务满意度';
COMMENT ON COLUMN public.pu_supplier_eval.product_qual_score IS '产品质量';
COMMENT ON COLUMN public.pu_supplier_eval.after_sale_score IS '产品售后';
COMMENT ON COLUMN public.pu_supplier_eval.creator_id IS '创建人';
COMMENT ON COLUMN public.pu_supplier_eval.create_time IS '创建时间';
