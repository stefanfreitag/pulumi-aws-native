// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ssm

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::SSM::Document resource is an SSM document in AWS Systems Manager that defines the actions that Systems Manager performs, which can be used to set up and run commands on your instances.
func LookupDocument(ctx *pulumi.Context, args *LookupDocumentArgs, opts ...pulumi.InvokeOption) (*LookupDocumentResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDocumentResult
	err := ctx.Invoke("aws-native:ssm:getDocument", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDocumentArgs struct {
	// A name for the Systems Manager document.
	Name string `pulumi:"name"`
}

type LookupDocumentResult struct {
	// The content for the Systems Manager document in JSON, YAML or String format.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SSM::Document` for more information about the expected schema for this property.
	Content interface{} `pulumi:"content"`
	// Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.
	DocumentFormat *DocumentFormat `pulumi:"documentFormat"`
	// A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.
	Requires []DocumentRequires `pulumi:"requires"`
	// Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment.
	Tags []aws.Tag `pulumi:"tags"`
	// Specify a target type to define the kinds of resources the document can run on.
	TargetType *string `pulumi:"targetType"`
	// An optional field specifying the version of the artifact you are creating with the document. This value is unique across all versions of a document, and cannot be changed.
	VersionName *string `pulumi:"versionName"`
}

func LookupDocumentOutput(ctx *pulumi.Context, args LookupDocumentOutputArgs, opts ...pulumi.InvokeOption) LookupDocumentResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDocumentResult, error) {
			args := v.(LookupDocumentArgs)
			r, err := LookupDocument(ctx, &args, opts...)
			var s LookupDocumentResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDocumentResultOutput)
}

type LookupDocumentOutputArgs struct {
	// A name for the Systems Manager document.
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupDocumentOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDocumentArgs)(nil)).Elem()
}

type LookupDocumentResultOutput struct{ *pulumi.OutputState }

func (LookupDocumentResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDocumentResult)(nil)).Elem()
}

func (o LookupDocumentResultOutput) ToLookupDocumentResultOutput() LookupDocumentResultOutput {
	return o
}

func (o LookupDocumentResultOutput) ToLookupDocumentResultOutputWithContext(ctx context.Context) LookupDocumentResultOutput {
	return o
}

// The content for the Systems Manager document in JSON, YAML or String format.
//
// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SSM::Document` for more information about the expected schema for this property.
func (o LookupDocumentResultOutput) Content() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupDocumentResult) interface{} { return v.Content }).(pulumi.AnyOutput)
}

// Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.
func (o LookupDocumentResultOutput) DocumentFormat() DocumentFormatPtrOutput {
	return o.ApplyT(func(v LookupDocumentResult) *DocumentFormat { return v.DocumentFormat }).(DocumentFormatPtrOutput)
}

// A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.
func (o LookupDocumentResultOutput) Requires() DocumentRequiresArrayOutput {
	return o.ApplyT(func(v LookupDocumentResult) []DocumentRequires { return v.Requires }).(DocumentRequiresArrayOutput)
}

// Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment.
func (o LookupDocumentResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupDocumentResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

// Specify a target type to define the kinds of resources the document can run on.
func (o LookupDocumentResultOutput) TargetType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDocumentResult) *string { return v.TargetType }).(pulumi.StringPtrOutput)
}

// An optional field specifying the version of the artifact you are creating with the document. This value is unique across all versions of a document, and cannot be changed.
func (o LookupDocumentResultOutput) VersionName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDocumentResult) *string { return v.VersionName }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDocumentResultOutput{})
}
