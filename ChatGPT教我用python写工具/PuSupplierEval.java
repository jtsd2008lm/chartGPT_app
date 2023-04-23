@Data 
@EqualsAndHashCode(callSuper = false) 
@TableName("pu_supplier_eval") 
@ApiModel(value = "PuSupplierEval对象" ) 
public class PuSupplierEval implements Serializable {

  @ApiModelProperty(value = "主键")
  @TableId(value = "supplier_eval_id", type = IdType.ASSIGN_ID)
  private Long supplierEvalId;

  @ApiModelProperty(value = "考评时间")
  private Date evalDate;

  @ApiModelProperty(value = "季度")
  private String quater;

  @ApiModelProperty(value = "供应商名称")
  private String supplierName;

  @ApiModelProperty(value = "采购产品")
  private String product;

  @ApiModelProperty(value = "采购金额")
  private BigDecimal amt;

  @ApiModelProperty(value = "相关考评部门")
  private String evalDept;

  @ApiModelProperty(value = "价格")
  private BigDecimal priceScore;

  @ApiModelProperty(value = "服务满意度")
  private BigDecimal serviceStatScore;

  @ApiModelProperty(value = "产品质量")
  private BigDecimal productQualScore;

  @ApiModelProperty(value = "产品售后")
  private BigDecimal afterSaleScore;

  @ApiModelProperty(value = "创建人")
  private Long creatorId;

  @ApiModelProperty(value = "创建时间")
  private Date createTime;

}