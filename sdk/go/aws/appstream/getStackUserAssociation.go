// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appstream

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::AppStream::StackUserAssociation
func LookupStackUserAssociation(ctx *pulumi.Context, args *LookupStackUserAssociationArgs, opts ...pulumi.InvokeOption) (*LookupStackUserAssociationResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupStackUserAssociationResult
	err := ctx.Invoke("aws-native:appstream:getStackUserAssociation", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupStackUserAssociationArgs struct {
	Id string `pulumi:"id"`
}

type LookupStackUserAssociationResult struct {
	Id *string `pulumi:"id"`
}

func LookupStackUserAssociationOutput(ctx *pulumi.Context, args LookupStackUserAssociationOutputArgs, opts ...pulumi.InvokeOption) LookupStackUserAssociationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupStackUserAssociationResult, error) {
			args := v.(LookupStackUserAssociationArgs)
			r, err := LookupStackUserAssociation(ctx, &args, opts...)
			var s LookupStackUserAssociationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupStackUserAssociationResultOutput)
}

type LookupStackUserAssociationOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupStackUserAssociationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupStackUserAssociationArgs)(nil)).Elem()
}

type LookupStackUserAssociationResultOutput struct{ *pulumi.OutputState }

func (LookupStackUserAssociationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupStackUserAssociationResult)(nil)).Elem()
}

func (o LookupStackUserAssociationResultOutput) ToLookupStackUserAssociationResultOutput() LookupStackUserAssociationResultOutput {
	return o
}

func (o LookupStackUserAssociationResultOutput) ToLookupStackUserAssociationResultOutputWithContext(ctx context.Context) LookupStackUserAssociationResultOutput {
	return o
}

func (o LookupStackUserAssociationResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupStackUserAssociationResult] {
	return pulumix.Output[LookupStackUserAssociationResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupStackUserAssociationResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStackUserAssociationResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupStackUserAssociationResultOutput{})
}
