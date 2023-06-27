// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lakeformation

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::LakeFormation::Permissions
func LookupPermissions(ctx *pulumi.Context, args *LookupPermissionsArgs, opts ...pulumi.InvokeOption) (*LookupPermissionsResult, error) {
	var rv LookupPermissionsResult
	err := ctx.Invoke("aws-native:lakeformation:getPermissions", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupPermissionsArgs struct {
	Id string `pulumi:"id"`
}

type LookupPermissionsResult struct {
	DataLakePrincipal          *PermissionsDataLakePrincipal `pulumi:"dataLakePrincipal"`
	Id                         *string                       `pulumi:"id"`
	Permissions                []string                      `pulumi:"permissions"`
	PermissionsWithGrantOption []string                      `pulumi:"permissionsWithGrantOption"`
	Resource                   *PermissionsResource          `pulumi:"resource"`
}

func LookupPermissionsOutput(ctx *pulumi.Context, args LookupPermissionsOutputArgs, opts ...pulumi.InvokeOption) LookupPermissionsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPermissionsResult, error) {
			args := v.(LookupPermissionsArgs)
			r, err := LookupPermissions(ctx, &args, opts...)
			var s LookupPermissionsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupPermissionsResultOutput)
}

type LookupPermissionsOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupPermissionsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPermissionsArgs)(nil)).Elem()
}

type LookupPermissionsResultOutput struct{ *pulumi.OutputState }

func (LookupPermissionsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPermissionsResult)(nil)).Elem()
}

func (o LookupPermissionsResultOutput) ToLookupPermissionsResultOutput() LookupPermissionsResultOutput {
	return o
}

func (o LookupPermissionsResultOutput) ToLookupPermissionsResultOutputWithContext(ctx context.Context) LookupPermissionsResultOutput {
	return o
}

func (o LookupPermissionsResultOutput) DataLakePrincipal() PermissionsDataLakePrincipalPtrOutput {
	return o.ApplyT(func(v LookupPermissionsResult) *PermissionsDataLakePrincipal { return v.DataLakePrincipal }).(PermissionsDataLakePrincipalPtrOutput)
}

func (o LookupPermissionsResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPermissionsResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupPermissionsResultOutput) Permissions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupPermissionsResult) []string { return v.Permissions }).(pulumi.StringArrayOutput)
}

func (o LookupPermissionsResultOutput) PermissionsWithGrantOption() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupPermissionsResult) []string { return v.PermissionsWithGrantOption }).(pulumi.StringArrayOutput)
}

func (o LookupPermissionsResultOutput) Resource() PermissionsResourcePtrOutput {
	return o.ApplyT(func(v LookupPermissionsResult) *PermissionsResource { return v.Resource }).(PermissionsResourcePtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPermissionsResultOutput{})
}
