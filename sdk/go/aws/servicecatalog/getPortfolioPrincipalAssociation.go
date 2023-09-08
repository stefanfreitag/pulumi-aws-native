// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package servicecatalog

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::ServiceCatalog::PortfolioPrincipalAssociation
func LookupPortfolioPrincipalAssociation(ctx *pulumi.Context, args *LookupPortfolioPrincipalAssociationArgs, opts ...pulumi.InvokeOption) (*LookupPortfolioPrincipalAssociationResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupPortfolioPrincipalAssociationResult
	err := ctx.Invoke("aws-native:servicecatalog:getPortfolioPrincipalAssociation", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupPortfolioPrincipalAssociationArgs struct {
	Id string `pulumi:"id"`
}

type LookupPortfolioPrincipalAssociationResult struct {
	Id *string `pulumi:"id"`
}

func LookupPortfolioPrincipalAssociationOutput(ctx *pulumi.Context, args LookupPortfolioPrincipalAssociationOutputArgs, opts ...pulumi.InvokeOption) LookupPortfolioPrincipalAssociationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPortfolioPrincipalAssociationResult, error) {
			args := v.(LookupPortfolioPrincipalAssociationArgs)
			r, err := LookupPortfolioPrincipalAssociation(ctx, &args, opts...)
			var s LookupPortfolioPrincipalAssociationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupPortfolioPrincipalAssociationResultOutput)
}

type LookupPortfolioPrincipalAssociationOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupPortfolioPrincipalAssociationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPortfolioPrincipalAssociationArgs)(nil)).Elem()
}

type LookupPortfolioPrincipalAssociationResultOutput struct{ *pulumi.OutputState }

func (LookupPortfolioPrincipalAssociationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPortfolioPrincipalAssociationResult)(nil)).Elem()
}

func (o LookupPortfolioPrincipalAssociationResultOutput) ToLookupPortfolioPrincipalAssociationResultOutput() LookupPortfolioPrincipalAssociationResultOutput {
	return o
}

func (o LookupPortfolioPrincipalAssociationResultOutput) ToLookupPortfolioPrincipalAssociationResultOutputWithContext(ctx context.Context) LookupPortfolioPrincipalAssociationResultOutput {
	return o
}

func (o LookupPortfolioPrincipalAssociationResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupPortfolioPrincipalAssociationResult] {
	return pulumix.Output[LookupPortfolioPrincipalAssociationResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupPortfolioPrincipalAssociationResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPortfolioPrincipalAssociationResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPortfolioPrincipalAssociationResultOutput{})
}
