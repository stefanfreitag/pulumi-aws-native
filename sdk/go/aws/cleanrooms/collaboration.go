// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cleanrooms

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Represents a collaboration between AWS accounts that allows for secure data collaboration
type Collaboration struct {
	pulumi.CustomResourceState

	Arn                         pulumi.StringOutput                          `pulumi:"arn"`
	CollaborationIdentifier     pulumi.StringOutput                          `pulumi:"collaborationIdentifier"`
	CreatorDisplayName          pulumi.StringOutput                          `pulumi:"creatorDisplayName"`
	CreatorMemberAbilities      CollaborationMemberAbilityArrayOutput        `pulumi:"creatorMemberAbilities"`
	CreatorPaymentConfiguration CollaborationPaymentConfigurationPtrOutput   `pulumi:"creatorPaymentConfiguration"`
	DataEncryptionMetadata      CollaborationDataEncryptionMetadataPtrOutput `pulumi:"dataEncryptionMetadata"`
	Description                 pulumi.StringOutput                          `pulumi:"description"`
	Members                     CollaborationMemberSpecificationArrayOutput  `pulumi:"members"`
	Name                        pulumi.StringOutput                          `pulumi:"name"`
	QueryLogStatus              CollaborationQueryLogStatusOutput            `pulumi:"queryLogStatus"`
	// An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewCollaboration registers a new resource with the given unique name, arguments, and options.
func NewCollaboration(ctx *pulumi.Context,
	name string, args *CollaborationArgs, opts ...pulumi.ResourceOption) (*Collaboration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CreatorDisplayName == nil {
		return nil, errors.New("invalid value for required argument 'CreatorDisplayName'")
	}
	if args.CreatorMemberAbilities == nil {
		return nil, errors.New("invalid value for required argument 'CreatorMemberAbilities'")
	}
	if args.Description == nil {
		return nil, errors.New("invalid value for required argument 'Description'")
	}
	if args.Members == nil {
		return nil, errors.New("invalid value for required argument 'Members'")
	}
	if args.QueryLogStatus == nil {
		return nil, errors.New("invalid value for required argument 'QueryLogStatus'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"creatorDisplayName",
		"creatorMemberAbilities[*]",
		"creatorPaymentConfiguration",
		"dataEncryptionMetadata",
		"members[*]",
		"queryLogStatus",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Collaboration
	err := ctx.RegisterResource("aws-native:cleanrooms:Collaboration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCollaboration gets an existing Collaboration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCollaboration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CollaborationState, opts ...pulumi.ResourceOption) (*Collaboration, error) {
	var resource Collaboration
	err := ctx.ReadResource("aws-native:cleanrooms:Collaboration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Collaboration resources.
type collaborationState struct {
}

type CollaborationState struct {
}

func (CollaborationState) ElementType() reflect.Type {
	return reflect.TypeOf((*collaborationState)(nil)).Elem()
}

type collaborationArgs struct {
	CreatorDisplayName          string                               `pulumi:"creatorDisplayName"`
	CreatorMemberAbilities      []CollaborationMemberAbility         `pulumi:"creatorMemberAbilities"`
	CreatorPaymentConfiguration *CollaborationPaymentConfiguration   `pulumi:"creatorPaymentConfiguration"`
	DataEncryptionMetadata      *CollaborationDataEncryptionMetadata `pulumi:"dataEncryptionMetadata"`
	Description                 string                               `pulumi:"description"`
	Members                     []CollaborationMemberSpecification   `pulumi:"members"`
	Name                        *string                              `pulumi:"name"`
	QueryLogStatus              CollaborationQueryLogStatus          `pulumi:"queryLogStatus"`
	// An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a Collaboration resource.
type CollaborationArgs struct {
	CreatorDisplayName          pulumi.StringInput
	CreatorMemberAbilities      CollaborationMemberAbilityArrayInput
	CreatorPaymentConfiguration CollaborationPaymentConfigurationPtrInput
	DataEncryptionMetadata      CollaborationDataEncryptionMetadataPtrInput
	Description                 pulumi.StringInput
	Members                     CollaborationMemberSpecificationArrayInput
	Name                        pulumi.StringPtrInput
	QueryLogStatus              CollaborationQueryLogStatusInput
	// An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
	Tags aws.TagArrayInput
}

func (CollaborationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*collaborationArgs)(nil)).Elem()
}

type CollaborationInput interface {
	pulumi.Input

	ToCollaborationOutput() CollaborationOutput
	ToCollaborationOutputWithContext(ctx context.Context) CollaborationOutput
}

func (*Collaboration) ElementType() reflect.Type {
	return reflect.TypeOf((**Collaboration)(nil)).Elem()
}

func (i *Collaboration) ToCollaborationOutput() CollaborationOutput {
	return i.ToCollaborationOutputWithContext(context.Background())
}

func (i *Collaboration) ToCollaborationOutputWithContext(ctx context.Context) CollaborationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CollaborationOutput)
}

type CollaborationOutput struct{ *pulumi.OutputState }

func (CollaborationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Collaboration)(nil)).Elem()
}

func (o CollaborationOutput) ToCollaborationOutput() CollaborationOutput {
	return o
}

func (o CollaborationOutput) ToCollaborationOutputWithContext(ctx context.Context) CollaborationOutput {
	return o
}

func (o CollaborationOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Collaboration) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o CollaborationOutput) CollaborationIdentifier() pulumi.StringOutput {
	return o.ApplyT(func(v *Collaboration) pulumi.StringOutput { return v.CollaborationIdentifier }).(pulumi.StringOutput)
}

func (o CollaborationOutput) CreatorDisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v *Collaboration) pulumi.StringOutput { return v.CreatorDisplayName }).(pulumi.StringOutput)
}

func (o CollaborationOutput) CreatorMemberAbilities() CollaborationMemberAbilityArrayOutput {
	return o.ApplyT(func(v *Collaboration) CollaborationMemberAbilityArrayOutput { return v.CreatorMemberAbilities }).(CollaborationMemberAbilityArrayOutput)
}

func (o CollaborationOutput) CreatorPaymentConfiguration() CollaborationPaymentConfigurationPtrOutput {
	return o.ApplyT(func(v *Collaboration) CollaborationPaymentConfigurationPtrOutput {
		return v.CreatorPaymentConfiguration
	}).(CollaborationPaymentConfigurationPtrOutput)
}

func (o CollaborationOutput) DataEncryptionMetadata() CollaborationDataEncryptionMetadataPtrOutput {
	return o.ApplyT(func(v *Collaboration) CollaborationDataEncryptionMetadataPtrOutput { return v.DataEncryptionMetadata }).(CollaborationDataEncryptionMetadataPtrOutput)
}

func (o CollaborationOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *Collaboration) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

func (o CollaborationOutput) Members() CollaborationMemberSpecificationArrayOutput {
	return o.ApplyT(func(v *Collaboration) CollaborationMemberSpecificationArrayOutput { return v.Members }).(CollaborationMemberSpecificationArrayOutput)
}

func (o CollaborationOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Collaboration) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o CollaborationOutput) QueryLogStatus() CollaborationQueryLogStatusOutput {
	return o.ApplyT(func(v *Collaboration) CollaborationQueryLogStatusOutput { return v.QueryLogStatus }).(CollaborationQueryLogStatusOutput)
}

// An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
func (o CollaborationOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *Collaboration) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CollaborationInput)(nil)).Elem(), &Collaboration{})
	pulumi.RegisterOutputType(CollaborationOutput{})
}
