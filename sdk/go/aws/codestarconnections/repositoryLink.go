// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package codestarconnections

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Schema for AWS::CodeStarConnections::RepositoryLink resource which is used to aggregate repository metadata relevant to synchronizing source provider content to AWS Resources.
type RepositoryLink struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the CodeStarConnection. The ARN is used as the connection reference when the connection is shared between AWS services.
	ConnectionArn pulumi.StringOutput `pulumi:"connectionArn"`
	// The ARN of the KMS key that the customer can optionally specify to use to encrypt RepositoryLink properties. If not specified, a default key will be used.
	EncryptionKeyArn pulumi.StringPtrOutput `pulumi:"encryptionKeyArn"`
	// the ID of the entity that owns the repository.
	OwnerId pulumi.StringOutput `pulumi:"ownerId"`
	// The name of the external provider where your third-party code repository is configured.
	ProviderType pulumi.StringOutput `pulumi:"providerType"`
	// A unique Amazon Resource Name (ARN) to designate the repository link.
	RepositoryLinkArn pulumi.StringOutput `pulumi:"repositoryLinkArn"`
	// A UUID that uniquely identifies the RepositoryLink.
	RepositoryLinkId pulumi.StringOutput `pulumi:"repositoryLinkId"`
	// The repository for which the link is being created.
	RepositoryName pulumi.StringOutput `pulumi:"repositoryName"`
	// Specifies the tags applied to a RepositoryLink.
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewRepositoryLink registers a new resource with the given unique name, arguments, and options.
func NewRepositoryLink(ctx *pulumi.Context,
	name string, args *RepositoryLinkArgs, opts ...pulumi.ResourceOption) (*RepositoryLink, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ConnectionArn == nil {
		return nil, errors.New("invalid value for required argument 'ConnectionArn'")
	}
	if args.OwnerId == nil {
		return nil, errors.New("invalid value for required argument 'OwnerId'")
	}
	if args.RepositoryName == nil {
		return nil, errors.New("invalid value for required argument 'RepositoryName'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"ownerId",
		"repositoryName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource RepositoryLink
	err := ctx.RegisterResource("aws-native:codestarconnections:RepositoryLink", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRepositoryLink gets an existing RepositoryLink resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRepositoryLink(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RepositoryLinkState, opts ...pulumi.ResourceOption) (*RepositoryLink, error) {
	var resource RepositoryLink
	err := ctx.ReadResource("aws-native:codestarconnections:RepositoryLink", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RepositoryLink resources.
type repositoryLinkState struct {
}

type RepositoryLinkState struct {
}

func (RepositoryLinkState) ElementType() reflect.Type {
	return reflect.TypeOf((*repositoryLinkState)(nil)).Elem()
}

type repositoryLinkArgs struct {
	// The Amazon Resource Name (ARN) of the CodeStarConnection. The ARN is used as the connection reference when the connection is shared between AWS services.
	ConnectionArn string `pulumi:"connectionArn"`
	// The ARN of the KMS key that the customer can optionally specify to use to encrypt RepositoryLink properties. If not specified, a default key will be used.
	EncryptionKeyArn *string `pulumi:"encryptionKeyArn"`
	// the ID of the entity that owns the repository.
	OwnerId string `pulumi:"ownerId"`
	// The repository for which the link is being created.
	RepositoryName string `pulumi:"repositoryName"`
	// Specifies the tags applied to a RepositoryLink.
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a RepositoryLink resource.
type RepositoryLinkArgs struct {
	// The Amazon Resource Name (ARN) of the CodeStarConnection. The ARN is used as the connection reference when the connection is shared between AWS services.
	ConnectionArn pulumi.StringInput
	// The ARN of the KMS key that the customer can optionally specify to use to encrypt RepositoryLink properties. If not specified, a default key will be used.
	EncryptionKeyArn pulumi.StringPtrInput
	// the ID of the entity that owns the repository.
	OwnerId pulumi.StringInput
	// The repository for which the link is being created.
	RepositoryName pulumi.StringInput
	// Specifies the tags applied to a RepositoryLink.
	Tags aws.TagArrayInput
}

func (RepositoryLinkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*repositoryLinkArgs)(nil)).Elem()
}

type RepositoryLinkInput interface {
	pulumi.Input

	ToRepositoryLinkOutput() RepositoryLinkOutput
	ToRepositoryLinkOutputWithContext(ctx context.Context) RepositoryLinkOutput
}

func (*RepositoryLink) ElementType() reflect.Type {
	return reflect.TypeOf((**RepositoryLink)(nil)).Elem()
}

func (i *RepositoryLink) ToRepositoryLinkOutput() RepositoryLinkOutput {
	return i.ToRepositoryLinkOutputWithContext(context.Background())
}

func (i *RepositoryLink) ToRepositoryLinkOutputWithContext(ctx context.Context) RepositoryLinkOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RepositoryLinkOutput)
}

type RepositoryLinkOutput struct{ *pulumi.OutputState }

func (RepositoryLinkOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RepositoryLink)(nil)).Elem()
}

func (o RepositoryLinkOutput) ToRepositoryLinkOutput() RepositoryLinkOutput {
	return o
}

func (o RepositoryLinkOutput) ToRepositoryLinkOutputWithContext(ctx context.Context) RepositoryLinkOutput {
	return o
}

// The Amazon Resource Name (ARN) of the CodeStarConnection. The ARN is used as the connection reference when the connection is shared between AWS services.
func (o RepositoryLinkOutput) ConnectionArn() pulumi.StringOutput {
	return o.ApplyT(func(v *RepositoryLink) pulumi.StringOutput { return v.ConnectionArn }).(pulumi.StringOutput)
}

// The ARN of the KMS key that the customer can optionally specify to use to encrypt RepositoryLink properties. If not specified, a default key will be used.
func (o RepositoryLinkOutput) EncryptionKeyArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RepositoryLink) pulumi.StringPtrOutput { return v.EncryptionKeyArn }).(pulumi.StringPtrOutput)
}

// the ID of the entity that owns the repository.
func (o RepositoryLinkOutput) OwnerId() pulumi.StringOutput {
	return o.ApplyT(func(v *RepositoryLink) pulumi.StringOutput { return v.OwnerId }).(pulumi.StringOutput)
}

// The name of the external provider where your third-party code repository is configured.
func (o RepositoryLinkOutput) ProviderType() pulumi.StringOutput {
	return o.ApplyT(func(v *RepositoryLink) pulumi.StringOutput { return v.ProviderType }).(pulumi.StringOutput)
}

// A unique Amazon Resource Name (ARN) to designate the repository link.
func (o RepositoryLinkOutput) RepositoryLinkArn() pulumi.StringOutput {
	return o.ApplyT(func(v *RepositoryLink) pulumi.StringOutput { return v.RepositoryLinkArn }).(pulumi.StringOutput)
}

// A UUID that uniquely identifies the RepositoryLink.
func (o RepositoryLinkOutput) RepositoryLinkId() pulumi.StringOutput {
	return o.ApplyT(func(v *RepositoryLink) pulumi.StringOutput { return v.RepositoryLinkId }).(pulumi.StringOutput)
}

// The repository for which the link is being created.
func (o RepositoryLinkOutput) RepositoryName() pulumi.StringOutput {
	return o.ApplyT(func(v *RepositoryLink) pulumi.StringOutput { return v.RepositoryName }).(pulumi.StringOutput)
}

// Specifies the tags applied to a RepositoryLink.
func (o RepositoryLinkOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *RepositoryLink) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RepositoryLinkInput)(nil)).Elem(), &RepositoryLink{})
	pulumi.RegisterOutputType(RepositoryLinkOutput{})
}
