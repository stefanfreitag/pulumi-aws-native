// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package glue

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Glue::Classifier
//
// Deprecated: Classifier is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Classifier struct {
	pulumi.CustomResourceState

	CsvClassifier  ClassifierCsvClassifierPtrOutput  `pulumi:"csvClassifier"`
	GrokClassifier ClassifierGrokClassifierPtrOutput `pulumi:"grokClassifier"`
	JsonClassifier ClassifierJsonClassifierPtrOutput `pulumi:"jsonClassifier"`
	XMLClassifier  ClassifierXMLClassifierPtrOutput  `pulumi:"xMLClassifier"`
}

// NewClassifier registers a new resource with the given unique name, arguments, and options.
func NewClassifier(ctx *pulumi.Context,
	name string, args *ClassifierArgs, opts ...pulumi.ResourceOption) (*Classifier, error) {
	if args == nil {
		args = &ClassifierArgs{}
	}

	var resource Classifier
	err := ctx.RegisterResource("aws-native:glue:Classifier", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetClassifier gets an existing Classifier resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetClassifier(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ClassifierState, opts ...pulumi.ResourceOption) (*Classifier, error) {
	var resource Classifier
	err := ctx.ReadResource("aws-native:glue:Classifier", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Classifier resources.
type classifierState struct {
}

type ClassifierState struct {
}

func (ClassifierState) ElementType() reflect.Type {
	return reflect.TypeOf((*classifierState)(nil)).Elem()
}

type classifierArgs struct {
	CsvClassifier  *ClassifierCsvClassifier  `pulumi:"csvClassifier"`
	GrokClassifier *ClassifierGrokClassifier `pulumi:"grokClassifier"`
	JsonClassifier *ClassifierJsonClassifier `pulumi:"jsonClassifier"`
	XMLClassifier  *ClassifierXMLClassifier  `pulumi:"xMLClassifier"`
}

// The set of arguments for constructing a Classifier resource.
type ClassifierArgs struct {
	CsvClassifier  ClassifierCsvClassifierPtrInput
	GrokClassifier ClassifierGrokClassifierPtrInput
	JsonClassifier ClassifierJsonClassifierPtrInput
	XMLClassifier  ClassifierXMLClassifierPtrInput
}

func (ClassifierArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*classifierArgs)(nil)).Elem()
}

type ClassifierInput interface {
	pulumi.Input

	ToClassifierOutput() ClassifierOutput
	ToClassifierOutputWithContext(ctx context.Context) ClassifierOutput
}

func (*Classifier) ElementType() reflect.Type {
	return reflect.TypeOf((*Classifier)(nil))
}

func (i *Classifier) ToClassifierOutput() ClassifierOutput {
	return i.ToClassifierOutputWithContext(context.Background())
}

func (i *Classifier) ToClassifierOutputWithContext(ctx context.Context) ClassifierOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClassifierOutput)
}

type ClassifierOutput struct{ *pulumi.OutputState }

func (ClassifierOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Classifier)(nil))
}

func (o ClassifierOutput) ToClassifierOutput() ClassifierOutput {
	return o
}

func (o ClassifierOutput) ToClassifierOutputWithContext(ctx context.Context) ClassifierOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ClassifierOutput{})
}
