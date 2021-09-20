// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package route53resolver

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation.
type ResolverQueryLoggingConfigAssociation struct {
	pulumi.CustomResourceState

	// Rfc3339TimeString
	CreationTime pulumi.StringOutput `pulumi:"creationTime"`
	// ResolverQueryLogConfigAssociationError
	Error ResolverQueryLoggingConfigAssociationErrorOutput `pulumi:"error"`
	// ResolverQueryLogConfigAssociationErrorMessage
	ErrorMessage pulumi.StringOutput `pulumi:"errorMessage"`
	// ResolverQueryLogConfigId
	ResolverQueryLogConfigId pulumi.StringPtrOutput `pulumi:"resolverQueryLogConfigId"`
	// ResourceId
	ResourceId pulumi.StringPtrOutput `pulumi:"resourceId"`
	// ResolverQueryLogConfigAssociationStatus
	Status ResolverQueryLoggingConfigAssociationStatusOutput `pulumi:"status"`
}

// NewResolverQueryLoggingConfigAssociation registers a new resource with the given unique name, arguments, and options.
func NewResolverQueryLoggingConfigAssociation(ctx *pulumi.Context,
	name string, args *ResolverQueryLoggingConfigAssociationArgs, opts ...pulumi.ResourceOption) (*ResolverQueryLoggingConfigAssociation, error) {
	if args == nil {
		args = &ResolverQueryLoggingConfigAssociationArgs{}
	}

	var resource ResolverQueryLoggingConfigAssociation
	err := ctx.RegisterResource("aws-native:route53resolver:ResolverQueryLoggingConfigAssociation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResolverQueryLoggingConfigAssociation gets an existing ResolverQueryLoggingConfigAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResolverQueryLoggingConfigAssociation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResolverQueryLoggingConfigAssociationState, opts ...pulumi.ResourceOption) (*ResolverQueryLoggingConfigAssociation, error) {
	var resource ResolverQueryLoggingConfigAssociation
	err := ctx.ReadResource("aws-native:route53resolver:ResolverQueryLoggingConfigAssociation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ResolverQueryLoggingConfigAssociation resources.
type resolverQueryLoggingConfigAssociationState struct {
}

type ResolverQueryLoggingConfigAssociationState struct {
}

func (ResolverQueryLoggingConfigAssociationState) ElementType() reflect.Type {
	return reflect.TypeOf((*resolverQueryLoggingConfigAssociationState)(nil)).Elem()
}

type resolverQueryLoggingConfigAssociationArgs struct {
	// ResolverQueryLogConfigId
	ResolverQueryLogConfigId *string `pulumi:"resolverQueryLogConfigId"`
	// ResourceId
	ResourceId *string `pulumi:"resourceId"`
}

// The set of arguments for constructing a ResolverQueryLoggingConfigAssociation resource.
type ResolverQueryLoggingConfigAssociationArgs struct {
	// ResolverQueryLogConfigId
	ResolverQueryLogConfigId pulumi.StringPtrInput
	// ResourceId
	ResourceId pulumi.StringPtrInput
}

func (ResolverQueryLoggingConfigAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*resolverQueryLoggingConfigAssociationArgs)(nil)).Elem()
}

type ResolverQueryLoggingConfigAssociationInput interface {
	pulumi.Input

	ToResolverQueryLoggingConfigAssociationOutput() ResolverQueryLoggingConfigAssociationOutput
	ToResolverQueryLoggingConfigAssociationOutputWithContext(ctx context.Context) ResolverQueryLoggingConfigAssociationOutput
}

func (*ResolverQueryLoggingConfigAssociation) ElementType() reflect.Type {
	return reflect.TypeOf((*ResolverQueryLoggingConfigAssociation)(nil))
}

func (i *ResolverQueryLoggingConfigAssociation) ToResolverQueryLoggingConfigAssociationOutput() ResolverQueryLoggingConfigAssociationOutput {
	return i.ToResolverQueryLoggingConfigAssociationOutputWithContext(context.Background())
}

func (i *ResolverQueryLoggingConfigAssociation) ToResolverQueryLoggingConfigAssociationOutputWithContext(ctx context.Context) ResolverQueryLoggingConfigAssociationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ResolverQueryLoggingConfigAssociationOutput)
}

type ResolverQueryLoggingConfigAssociationOutput struct{ *pulumi.OutputState }

func (ResolverQueryLoggingConfigAssociationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ResolverQueryLoggingConfigAssociation)(nil))
}

func (o ResolverQueryLoggingConfigAssociationOutput) ToResolverQueryLoggingConfigAssociationOutput() ResolverQueryLoggingConfigAssociationOutput {
	return o
}

func (o ResolverQueryLoggingConfigAssociationOutput) ToResolverQueryLoggingConfigAssociationOutputWithContext(ctx context.Context) ResolverQueryLoggingConfigAssociationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ResolverQueryLoggingConfigAssociationOutput{})
}
