// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package quicksight

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of the AWS::QuickSight::DataSource Resource Type.
func LookupDataSource(ctx *pulumi.Context, args *LookupDataSourceArgs, opts ...pulumi.InvokeOption) (*LookupDataSourceResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDataSourceResult
	err := ctx.Invoke("aws-native:quicksight:getDataSource", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDataSourceArgs struct {
	AwsAccountId string `pulumi:"awsAccountId"`
	DataSourceId string `pulumi:"dataSourceId"`
}

type LookupDataSourceResult struct {
	// <p>A set of alternate data source parameters that you want to share for the credentials
	//             stored with this data source. The credentials are applied in tandem with the data source
	//             parameters when you copy a data source by using a create or update request. The API
	//             operation compares the <code>DataSourceParameters</code> structure that's in the request
	//             with the structures in the <code>AlternateDataSourceParameters</code> allow list. If the
	//             structures are an exact match, the request is allowed to use the credentials from this
	//             existing data source. If the <code>AlternateDataSourceParameters</code> list is null,
	//             the <code>Credentials</code> originally used with this <code>DataSourceParameters</code>
	//             are automatically allowed.</p>
	AlternateDataSourceParameters []DataSourceParameters `pulumi:"alternateDataSourceParameters"`
	// <p>The Amazon Resource Name (ARN) of the data source.</p>
	Arn *string `pulumi:"arn"`
	// <p>The time that this data source was created.</p>
	CreatedTime          *string               `pulumi:"createdTime"`
	DataSourceParameters *DataSourceParameters `pulumi:"dataSourceParameters"`
	ErrorInfo            *DataSourceErrorInfo  `pulumi:"errorInfo"`
	// <p>The last time that this data source was updated.</p>
	LastUpdatedTime *string `pulumi:"lastUpdatedTime"`
	// <p>A display name for the data source.</p>
	Name *string `pulumi:"name"`
	// <p>A list of resource permissions on the data source.</p>
	Permissions   []DataSourceResourcePermission `pulumi:"permissions"`
	SslProperties *DataSourceSslProperties       `pulumi:"sslProperties"`
	Status        *DataSourceResourceStatus      `pulumi:"status"`
	// <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.</p>
	Tags                    []DataSourceTag                    `pulumi:"tags"`
	VpcConnectionProperties *DataSourceVpcConnectionProperties `pulumi:"vpcConnectionProperties"`
}

func LookupDataSourceOutput(ctx *pulumi.Context, args LookupDataSourceOutputArgs, opts ...pulumi.InvokeOption) LookupDataSourceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDataSourceResult, error) {
			args := v.(LookupDataSourceArgs)
			r, err := LookupDataSource(ctx, &args, opts...)
			var s LookupDataSourceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDataSourceResultOutput)
}

type LookupDataSourceOutputArgs struct {
	AwsAccountId pulumi.StringInput `pulumi:"awsAccountId"`
	DataSourceId pulumi.StringInput `pulumi:"dataSourceId"`
}

func (LookupDataSourceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataSourceArgs)(nil)).Elem()
}

type LookupDataSourceResultOutput struct{ *pulumi.OutputState }

func (LookupDataSourceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataSourceResult)(nil)).Elem()
}

func (o LookupDataSourceResultOutput) ToLookupDataSourceResultOutput() LookupDataSourceResultOutput {
	return o
}

func (o LookupDataSourceResultOutput) ToLookupDataSourceResultOutputWithContext(ctx context.Context) LookupDataSourceResultOutput {
	return o
}

func (o LookupDataSourceResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupDataSourceResult] {
	return pulumix.Output[LookupDataSourceResult]{
		OutputState: o.OutputState,
	}
}

// <p>A set of alternate data source parameters that you want to share for the credentials
//
//	stored with this data source. The credentials are applied in tandem with the data source
//	parameters when you copy a data source by using a create or update request. The API
//	operation compares the <code>DataSourceParameters</code> structure that's in the request
//	with the structures in the <code>AlternateDataSourceParameters</code> allow list. If the
//	structures are an exact match, the request is allowed to use the credentials from this
//	existing data source. If the <code>AlternateDataSourceParameters</code> list is null,
//	the <code>Credentials</code> originally used with this <code>DataSourceParameters</code>
//	are automatically allowed.</p>
func (o LookupDataSourceResultOutput) AlternateDataSourceParameters() DataSourceParametersArrayOutput {
	return o.ApplyT(func(v LookupDataSourceResult) []DataSourceParameters { return v.AlternateDataSourceParameters }).(DataSourceParametersArrayOutput)
}

// <p>The Amazon Resource Name (ARN) of the data source.</p>
func (o LookupDataSourceResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// <p>The time that this data source was created.</p>
func (o LookupDataSourceResultOutput) CreatedTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *string { return v.CreatedTime }).(pulumi.StringPtrOutput)
}

func (o LookupDataSourceResultOutput) DataSourceParameters() DataSourceParametersPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *DataSourceParameters { return v.DataSourceParameters }).(DataSourceParametersPtrOutput)
}

func (o LookupDataSourceResultOutput) ErrorInfo() DataSourceErrorInfoPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *DataSourceErrorInfo { return v.ErrorInfo }).(DataSourceErrorInfoPtrOutput)
}

// <p>The last time that this data source was updated.</p>
func (o LookupDataSourceResultOutput) LastUpdatedTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *string { return v.LastUpdatedTime }).(pulumi.StringPtrOutput)
}

// <p>A display name for the data source.</p>
func (o LookupDataSourceResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// <p>A list of resource permissions on the data source.</p>
func (o LookupDataSourceResultOutput) Permissions() DataSourceResourcePermissionArrayOutput {
	return o.ApplyT(func(v LookupDataSourceResult) []DataSourceResourcePermission { return v.Permissions }).(DataSourceResourcePermissionArrayOutput)
}

func (o LookupDataSourceResultOutput) SslProperties() DataSourceSslPropertiesPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *DataSourceSslProperties { return v.SslProperties }).(DataSourceSslPropertiesPtrOutput)
}

func (o LookupDataSourceResultOutput) Status() DataSourceResourceStatusPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *DataSourceResourceStatus { return v.Status }).(DataSourceResourceStatusPtrOutput)
}

// <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.</p>
func (o LookupDataSourceResultOutput) Tags() DataSourceTagArrayOutput {
	return o.ApplyT(func(v LookupDataSourceResult) []DataSourceTag { return v.Tags }).(DataSourceTagArrayOutput)
}

func (o LookupDataSourceResultOutput) VpcConnectionProperties() DataSourceVpcConnectionPropertiesPtrOutput {
	return o.ApplyT(func(v LookupDataSourceResult) *DataSourceVpcConnectionProperties { return v.VpcConnectionProperties }).(DataSourceVpcConnectionPropertiesPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDataSourceResultOutput{})
}
