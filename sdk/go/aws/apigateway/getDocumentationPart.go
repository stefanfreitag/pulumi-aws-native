// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::ApiGateway::DocumentationPart
func LookupDocumentationPart(ctx *pulumi.Context, args *LookupDocumentationPartArgs, opts ...pulumi.InvokeOption) (*LookupDocumentationPartResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDocumentationPartResult
	err := ctx.Invoke("aws-native:apigateway:getDocumentationPart", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDocumentationPartArgs struct {
	// The identifier of the documentation Part.
	DocumentationPartId string `pulumi:"documentationPartId"`
	// Identifier of the targeted API entity
	RestApiId string `pulumi:"restApiId"`
}

type LookupDocumentationPartResult struct {
	// The identifier of the documentation Part.
	DocumentationPartId *string `pulumi:"documentationPartId"`
	// The documentation content map of the targeted API entity.
	Properties *string `pulumi:"properties"`
}

func LookupDocumentationPartOutput(ctx *pulumi.Context, args LookupDocumentationPartOutputArgs, opts ...pulumi.InvokeOption) LookupDocumentationPartResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDocumentationPartResult, error) {
			args := v.(LookupDocumentationPartArgs)
			r, err := LookupDocumentationPart(ctx, &args, opts...)
			var s LookupDocumentationPartResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDocumentationPartResultOutput)
}

type LookupDocumentationPartOutputArgs struct {
	// The identifier of the documentation Part.
	DocumentationPartId pulumi.StringInput `pulumi:"documentationPartId"`
	// Identifier of the targeted API entity
	RestApiId pulumi.StringInput `pulumi:"restApiId"`
}

func (LookupDocumentationPartOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDocumentationPartArgs)(nil)).Elem()
}

type LookupDocumentationPartResultOutput struct{ *pulumi.OutputState }

func (LookupDocumentationPartResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDocumentationPartResult)(nil)).Elem()
}

func (o LookupDocumentationPartResultOutput) ToLookupDocumentationPartResultOutput() LookupDocumentationPartResultOutput {
	return o
}

func (o LookupDocumentationPartResultOutput) ToLookupDocumentationPartResultOutputWithContext(ctx context.Context) LookupDocumentationPartResultOutput {
	return o
}

func (o LookupDocumentationPartResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupDocumentationPartResult] {
	return pulumix.Output[LookupDocumentationPartResult]{
		OutputState: o.OutputState,
	}
}

// The identifier of the documentation Part.
func (o LookupDocumentationPartResultOutput) DocumentationPartId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDocumentationPartResult) *string { return v.DocumentationPartId }).(pulumi.StringPtrOutput)
}

// The documentation content map of the targeted API entity.
func (o LookupDocumentationPartResultOutput) Properties() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDocumentationPartResult) *string { return v.Properties }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDocumentationPartResultOutput{})
}
