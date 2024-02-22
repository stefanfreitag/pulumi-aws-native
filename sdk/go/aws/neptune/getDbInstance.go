// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package neptune

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Neptune::DBInstance
func LookupDbInstance(ctx *pulumi.Context, args *LookupDbInstanceArgs, opts ...pulumi.InvokeOption) (*LookupDbInstanceResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDbInstanceResult
	err := ctx.Invoke("aws-native:neptune:getDbInstance", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDbInstanceArgs struct {
	Id string `pulumi:"id"`
}

type LookupDbInstanceResult struct {
	AllowMajorVersionUpgrade   *bool     `pulumi:"allowMajorVersionUpgrade"`
	AutoMinorVersionUpgrade    *bool     `pulumi:"autoMinorVersionUpgrade"`
	DbInstanceClass            *string   `pulumi:"dbInstanceClass"`
	DbParameterGroupName       *string   `pulumi:"dbParameterGroupName"`
	Endpoint                   *string   `pulumi:"endpoint"`
	Id                         *string   `pulumi:"id"`
	Port                       *string   `pulumi:"port"`
	PreferredMaintenanceWindow *string   `pulumi:"preferredMaintenanceWindow"`
	Tags                       []aws.Tag `pulumi:"tags"`
}

func LookupDbInstanceOutput(ctx *pulumi.Context, args LookupDbInstanceOutputArgs, opts ...pulumi.InvokeOption) LookupDbInstanceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDbInstanceResult, error) {
			args := v.(LookupDbInstanceArgs)
			r, err := LookupDbInstance(ctx, &args, opts...)
			var s LookupDbInstanceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDbInstanceResultOutput)
}

type LookupDbInstanceOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupDbInstanceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDbInstanceArgs)(nil)).Elem()
}

type LookupDbInstanceResultOutput struct{ *pulumi.OutputState }

func (LookupDbInstanceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDbInstanceResult)(nil)).Elem()
}

func (o LookupDbInstanceResultOutput) ToLookupDbInstanceResultOutput() LookupDbInstanceResultOutput {
	return o
}

func (o LookupDbInstanceResultOutput) ToLookupDbInstanceResultOutputWithContext(ctx context.Context) LookupDbInstanceResultOutput {
	return o
}

func (o LookupDbInstanceResultOutput) AllowMajorVersionUpgrade() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDbInstanceResult) *bool { return v.AllowMajorVersionUpgrade }).(pulumi.BoolPtrOutput)
}

func (o LookupDbInstanceResultOutput) AutoMinorVersionUpgrade() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDbInstanceResult) *bool { return v.AutoMinorVersionUpgrade }).(pulumi.BoolPtrOutput)
}

func (o LookupDbInstanceResultOutput) DbInstanceClass() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDbInstanceResult) *string { return v.DbInstanceClass }).(pulumi.StringPtrOutput)
}

func (o LookupDbInstanceResultOutput) DbParameterGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDbInstanceResult) *string { return v.DbParameterGroupName }).(pulumi.StringPtrOutput)
}

func (o LookupDbInstanceResultOutput) Endpoint() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDbInstanceResult) *string { return v.Endpoint }).(pulumi.StringPtrOutput)
}

func (o LookupDbInstanceResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDbInstanceResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupDbInstanceResultOutput) Port() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDbInstanceResult) *string { return v.Port }).(pulumi.StringPtrOutput)
}

func (o LookupDbInstanceResultOutput) PreferredMaintenanceWindow() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDbInstanceResult) *string { return v.PreferredMaintenanceWindow }).(pulumi.StringPtrOutput)
}

func (o LookupDbInstanceResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupDbInstanceResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDbInstanceResultOutput{})
}
