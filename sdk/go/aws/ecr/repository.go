// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ecr

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::ECR::Repository resource specifies an Amazon Elastic Container Registry (Amazon ECR) repository, where users can push and pull Docker images. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html
type Repository struct {
	pulumi.CustomResourceState

	Arn                        pulumi.StringOutput                           `pulumi:"arn"`
	EncryptionConfiguration    RepositoryEncryptionConfigurationPtrOutput    `pulumi:"encryptionConfiguration"`
	ImageScanningConfiguration RepositoryImageScanningConfigurationPtrOutput `pulumi:"imageScanningConfiguration"`
	// The image tag mutability setting for the repository.
	ImageTagMutability RepositoryImageTagMutabilityPtrOutput `pulumi:"imageTagMutability"`
	LifecyclePolicy    RepositoryLifecyclePolicyPtrOutput    `pulumi:"lifecyclePolicy"`
	// The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html.
	RepositoryName pulumi.StringPtrOutput `pulumi:"repositoryName"`
	// The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html in the Amazon Elastic Container Registry User Guide.
	RepositoryPolicyText pulumi.AnyOutput    `pulumi:"repositoryPolicyText"`
	RepositoryUri        pulumi.StringOutput `pulumi:"repositoryUri"`
	// An array of key-value pairs to apply to this resource.
	Tags RepositoryTagArrayOutput `pulumi:"tags"`
}

// NewRepository registers a new resource with the given unique name, arguments, and options.
func NewRepository(ctx *pulumi.Context,
	name string, args *RepositoryArgs, opts ...pulumi.ResourceOption) (*Repository, error) {
	if args == nil {
		args = &RepositoryArgs{}
	}

	var resource Repository
	err := ctx.RegisterResource("aws-native:ecr:Repository", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRepository gets an existing Repository resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRepository(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RepositoryState, opts ...pulumi.ResourceOption) (*Repository, error) {
	var resource Repository
	err := ctx.ReadResource("aws-native:ecr:Repository", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Repository resources.
type repositoryState struct {
}

type RepositoryState struct {
}

func (RepositoryState) ElementType() reflect.Type {
	return reflect.TypeOf((*repositoryState)(nil)).Elem()
}

type repositoryArgs struct {
	EncryptionConfiguration    *RepositoryEncryptionConfiguration    `pulumi:"encryptionConfiguration"`
	ImageScanningConfiguration *RepositoryImageScanningConfiguration `pulumi:"imageScanningConfiguration"`
	// The image tag mutability setting for the repository.
	ImageTagMutability *RepositoryImageTagMutability `pulumi:"imageTagMutability"`
	LifecyclePolicy    *RepositoryLifecyclePolicy    `pulumi:"lifecyclePolicy"`
	// The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html.
	RepositoryName *string `pulumi:"repositoryName"`
	// The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html in the Amazon Elastic Container Registry User Guide.
	RepositoryPolicyText interface{} `pulumi:"repositoryPolicyText"`
	// An array of key-value pairs to apply to this resource.
	Tags []RepositoryTag `pulumi:"tags"`
}

// The set of arguments for constructing a Repository resource.
type RepositoryArgs struct {
	EncryptionConfiguration    RepositoryEncryptionConfigurationPtrInput
	ImageScanningConfiguration RepositoryImageScanningConfigurationPtrInput
	// The image tag mutability setting for the repository.
	ImageTagMutability RepositoryImageTagMutabilityPtrInput
	LifecyclePolicy    RepositoryLifecyclePolicyPtrInput
	// The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html.
	RepositoryName pulumi.StringPtrInput
	// The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html in the Amazon Elastic Container Registry User Guide.
	RepositoryPolicyText pulumi.Input
	// An array of key-value pairs to apply to this resource.
	Tags RepositoryTagArrayInput
}

func (RepositoryArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*repositoryArgs)(nil)).Elem()
}

type RepositoryInput interface {
	pulumi.Input

	ToRepositoryOutput() RepositoryOutput
	ToRepositoryOutputWithContext(ctx context.Context) RepositoryOutput
}

func (*Repository) ElementType() reflect.Type {
	return reflect.TypeOf((*Repository)(nil))
}

func (i *Repository) ToRepositoryOutput() RepositoryOutput {
	return i.ToRepositoryOutputWithContext(context.Background())
}

func (i *Repository) ToRepositoryOutputWithContext(ctx context.Context) RepositoryOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RepositoryOutput)
}

type RepositoryOutput struct{ *pulumi.OutputState }

func (RepositoryOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Repository)(nil))
}

func (o RepositoryOutput) ToRepositoryOutput() RepositoryOutput {
	return o
}

func (o RepositoryOutput) ToRepositoryOutputWithContext(ctx context.Context) RepositoryOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RepositoryInput)(nil)).Elem(), &Repository{})
	pulumi.RegisterOutputType(RepositoryOutput{})
}
