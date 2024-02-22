// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ssm

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::SSM::Document resource is an SSM document in AWS Systems Manager that defines the actions that Systems Manager performs, which can be used to set up and run commands on your instances.
type Document struct {
	pulumi.CustomResourceState

	// A list of key and value pairs that describe attachments to a version of a document.
	Attachments DocumentAttachmentsSourceArrayOutput `pulumi:"attachments"`
	// The content for the Systems Manager document in JSON, YAML or String format.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SSM::Document` for more information about the expected schema for this property.
	Content pulumi.AnyOutput `pulumi:"content"`
	// Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.
	DocumentFormat DocumentFormatPtrOutput `pulumi:"documentFormat"`
	// The type of document to create.
	DocumentType DocumentTypePtrOutput `pulumi:"documentType"`
	// A name for the Systems Manager document.
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.
	Requires DocumentRequiresArrayOutput `pulumi:"requires"`
	// Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment.
	Tags aws.TagArrayOutput `pulumi:"tags"`
	// Specify a target type to define the kinds of resources the document can run on.
	TargetType pulumi.StringPtrOutput `pulumi:"targetType"`
	// Update method - when set to 'Replace', the update will replace the existing document; when set to 'NewVersion', the update will create a new version.
	UpdateMethod DocumentUpdateMethodPtrOutput `pulumi:"updateMethod"`
	// An optional field specifying the version of the artifact you are creating with the document. This value is unique across all versions of a document, and cannot be changed.
	VersionName pulumi.StringPtrOutput `pulumi:"versionName"`
}

// NewDocument registers a new resource with the given unique name, arguments, and options.
func NewDocument(ctx *pulumi.Context,
	name string, args *DocumentArgs, opts ...pulumi.ResourceOption) (*Document, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Content == nil {
		return nil, errors.New("invalid value for required argument 'Content'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"documentType",
		"name",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Document
	err := ctx.RegisterResource("aws-native:ssm:Document", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDocument gets an existing Document resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDocument(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DocumentState, opts ...pulumi.ResourceOption) (*Document, error) {
	var resource Document
	err := ctx.ReadResource("aws-native:ssm:Document", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Document resources.
type documentState struct {
}

type DocumentState struct {
}

func (DocumentState) ElementType() reflect.Type {
	return reflect.TypeOf((*documentState)(nil)).Elem()
}

type documentArgs struct {
	// A list of key and value pairs that describe attachments to a version of a document.
	Attachments []DocumentAttachmentsSource `pulumi:"attachments"`
	// The content for the Systems Manager document in JSON, YAML or String format.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SSM::Document` for more information about the expected schema for this property.
	Content interface{} `pulumi:"content"`
	// Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.
	DocumentFormat *DocumentFormat `pulumi:"documentFormat"`
	// The type of document to create.
	DocumentType *DocumentType `pulumi:"documentType"`
	// A name for the Systems Manager document.
	Name *string `pulumi:"name"`
	// A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.
	Requires []DocumentRequires `pulumi:"requires"`
	// Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment.
	Tags []aws.Tag `pulumi:"tags"`
	// Specify a target type to define the kinds of resources the document can run on.
	TargetType *string `pulumi:"targetType"`
	// Update method - when set to 'Replace', the update will replace the existing document; when set to 'NewVersion', the update will create a new version.
	UpdateMethod *DocumentUpdateMethod `pulumi:"updateMethod"`
	// An optional field specifying the version of the artifact you are creating with the document. This value is unique across all versions of a document, and cannot be changed.
	VersionName *string `pulumi:"versionName"`
}

// The set of arguments for constructing a Document resource.
type DocumentArgs struct {
	// A list of key and value pairs that describe attachments to a version of a document.
	Attachments DocumentAttachmentsSourceArrayInput
	// The content for the Systems Manager document in JSON, YAML or String format.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SSM::Document` for more information about the expected schema for this property.
	Content pulumi.Input
	// Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.
	DocumentFormat DocumentFormatPtrInput
	// The type of document to create.
	DocumentType DocumentTypePtrInput
	// A name for the Systems Manager document.
	Name pulumi.StringPtrInput
	// A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.
	Requires DocumentRequiresArrayInput
	// Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment.
	Tags aws.TagArrayInput
	// Specify a target type to define the kinds of resources the document can run on.
	TargetType pulumi.StringPtrInput
	// Update method - when set to 'Replace', the update will replace the existing document; when set to 'NewVersion', the update will create a new version.
	UpdateMethod DocumentUpdateMethodPtrInput
	// An optional field specifying the version of the artifact you are creating with the document. This value is unique across all versions of a document, and cannot be changed.
	VersionName pulumi.StringPtrInput
}

func (DocumentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*documentArgs)(nil)).Elem()
}

type DocumentInput interface {
	pulumi.Input

	ToDocumentOutput() DocumentOutput
	ToDocumentOutputWithContext(ctx context.Context) DocumentOutput
}

func (*Document) ElementType() reflect.Type {
	return reflect.TypeOf((**Document)(nil)).Elem()
}

func (i *Document) ToDocumentOutput() DocumentOutput {
	return i.ToDocumentOutputWithContext(context.Background())
}

func (i *Document) ToDocumentOutputWithContext(ctx context.Context) DocumentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DocumentOutput)
}

type DocumentOutput struct{ *pulumi.OutputState }

func (DocumentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Document)(nil)).Elem()
}

func (o DocumentOutput) ToDocumentOutput() DocumentOutput {
	return o
}

func (o DocumentOutput) ToDocumentOutputWithContext(ctx context.Context) DocumentOutput {
	return o
}

// A list of key and value pairs that describe attachments to a version of a document.
func (o DocumentOutput) Attachments() DocumentAttachmentsSourceArrayOutput {
	return o.ApplyT(func(v *Document) DocumentAttachmentsSourceArrayOutput { return v.Attachments }).(DocumentAttachmentsSourceArrayOutput)
}

// The content for the Systems Manager document in JSON, YAML or String format.
//
// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SSM::Document` for more information about the expected schema for this property.
func (o DocumentOutput) Content() pulumi.AnyOutput {
	return o.ApplyT(func(v *Document) pulumi.AnyOutput { return v.Content }).(pulumi.AnyOutput)
}

// Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.
func (o DocumentOutput) DocumentFormat() DocumentFormatPtrOutput {
	return o.ApplyT(func(v *Document) DocumentFormatPtrOutput { return v.DocumentFormat }).(DocumentFormatPtrOutput)
}

// The type of document to create.
func (o DocumentOutput) DocumentType() DocumentTypePtrOutput {
	return o.ApplyT(func(v *Document) DocumentTypePtrOutput { return v.DocumentType }).(DocumentTypePtrOutput)
}

// A name for the Systems Manager document.
func (o DocumentOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Document) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

// A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.
func (o DocumentOutput) Requires() DocumentRequiresArrayOutput {
	return o.ApplyT(func(v *Document) DocumentRequiresArrayOutput { return v.Requires }).(DocumentRequiresArrayOutput)
}

// Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment.
func (o DocumentOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *Document) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

// Specify a target type to define the kinds of resources the document can run on.
func (o DocumentOutput) TargetType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Document) pulumi.StringPtrOutput { return v.TargetType }).(pulumi.StringPtrOutput)
}

// Update method - when set to 'Replace', the update will replace the existing document; when set to 'NewVersion', the update will create a new version.
func (o DocumentOutput) UpdateMethod() DocumentUpdateMethodPtrOutput {
	return o.ApplyT(func(v *Document) DocumentUpdateMethodPtrOutput { return v.UpdateMethod }).(DocumentUpdateMethodPtrOutput)
}

// An optional field specifying the version of the artifact you are creating with the document. This value is unique across all versions of a document, and cannot be changed.
func (o DocumentOutput) VersionName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Document) pulumi.StringPtrOutput { return v.VersionName }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DocumentInput)(nil)).Elem(), &Document{})
	pulumi.RegisterOutputType(DocumentOutput{})
}
