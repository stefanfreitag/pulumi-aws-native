// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package wafregional

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::WAFRegional::XssMatchSet
//
// Deprecated: XssMatchSet is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type XssMatchSet struct {
	pulumi.CustomResourceState

	Name           pulumi.StringOutput                 `pulumi:"name"`
	XssMatchTuples XssMatchSetXssMatchTupleArrayOutput `pulumi:"xssMatchTuples"`
}

// NewXssMatchSet registers a new resource with the given unique name, arguments, and options.
func NewXssMatchSet(ctx *pulumi.Context,
	name string, args *XssMatchSetArgs, opts ...pulumi.ResourceOption) (*XssMatchSet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource XssMatchSet
	err := ctx.RegisterResource("aws-native:wafregional:XssMatchSet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetXssMatchSet gets an existing XssMatchSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetXssMatchSet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *XssMatchSetState, opts ...pulumi.ResourceOption) (*XssMatchSet, error) {
	var resource XssMatchSet
	err := ctx.ReadResource("aws-native:wafregional:XssMatchSet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering XssMatchSet resources.
type xssMatchSetState struct {
}

type XssMatchSetState struct {
}

func (XssMatchSetState) ElementType() reflect.Type {
	return reflect.TypeOf((*xssMatchSetState)(nil)).Elem()
}

type xssMatchSetArgs struct {
	Name           string                     `pulumi:"name"`
	XssMatchTuples []XssMatchSetXssMatchTuple `pulumi:"xssMatchTuples"`
}

// The set of arguments for constructing a XssMatchSet resource.
type XssMatchSetArgs struct {
	Name           pulumi.StringInput
	XssMatchTuples XssMatchSetXssMatchTupleArrayInput
}

func (XssMatchSetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*xssMatchSetArgs)(nil)).Elem()
}

type XssMatchSetInput interface {
	pulumi.Input

	ToXssMatchSetOutput() XssMatchSetOutput
	ToXssMatchSetOutputWithContext(ctx context.Context) XssMatchSetOutput
}

func (*XssMatchSet) ElementType() reflect.Type {
	return reflect.TypeOf((*XssMatchSet)(nil))
}

func (i *XssMatchSet) ToXssMatchSetOutput() XssMatchSetOutput {
	return i.ToXssMatchSetOutputWithContext(context.Background())
}

func (i *XssMatchSet) ToXssMatchSetOutputWithContext(ctx context.Context) XssMatchSetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(XssMatchSetOutput)
}

type XssMatchSetOutput struct{ *pulumi.OutputState }

func (XssMatchSetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*XssMatchSet)(nil))
}

func (o XssMatchSetOutput) ToXssMatchSetOutput() XssMatchSetOutput {
	return o
}

func (o XssMatchSetOutput) ToXssMatchSetOutputWithContext(ctx context.Context) XssMatchSetOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(XssMatchSetOutput{})
}
