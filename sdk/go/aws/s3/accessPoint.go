// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package s3

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::S3::AccessPoint resource is an Amazon S3 resource type that you can use to access buckets.
type AccessPoint struct {
	pulumi.CustomResourceState

	// The alias of this Access Point. This alias can be used for compatibility purposes with other AWS services and third-party applications.
	Alias pulumi.StringOutput `pulumi:"alias"`
	// The Amazon Resource Name (ARN) of the specified accesspoint.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The name of the bucket that you want to associate this Access Point with.
	Bucket pulumi.StringOutput `pulumi:"bucket"`
	// The name you want to assign to this Access Point. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the access point name.
	Name pulumi.StringOutput `pulumi:"name"`
	// Indicates whether this Access Point allows access from the public Internet. If VpcConfiguration is specified for this Access Point, then NetworkOrigin is VPC, and the Access Point doesn't allow access from the public Internet. Otherwise, NetworkOrigin is Internet, and the Access Point allows access from the public Internet, subject to the Access Point and bucket access policies.
	NetworkOrigin AccessPointNetworkOriginOutput `pulumi:"networkOrigin"`
	// The Access Point Policy you want to apply to this access point.
	Policy       pulumi.AnyOutput `pulumi:"policy"`
	PolicyStatus pulumi.AnyOutput `pulumi:"policyStatus"`
	// The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.
	PublicAccessBlockConfiguration AccessPointPublicAccessBlockConfigurationPtrOutput `pulumi:"publicAccessBlockConfiguration"`
	// If you include this field, Amazon S3 restricts access to this Access Point to requests from the specified Virtual Private Cloud (VPC).
	VpcConfiguration AccessPointVpcConfigurationPtrOutput `pulumi:"vpcConfiguration"`
}

// NewAccessPoint registers a new resource with the given unique name, arguments, and options.
func NewAccessPoint(ctx *pulumi.Context,
	name string, args *AccessPointArgs, opts ...pulumi.ResourceOption) (*AccessPoint, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Bucket == nil {
		return nil, errors.New("invalid value for required argument 'Bucket'")
	}
	var resource AccessPoint
	err := ctx.RegisterResource("aws-native:s3:AccessPoint", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAccessPoint gets an existing AccessPoint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAccessPoint(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AccessPointState, opts ...pulumi.ResourceOption) (*AccessPoint, error) {
	var resource AccessPoint
	err := ctx.ReadResource("aws-native:s3:AccessPoint", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AccessPoint resources.
type accessPointState struct {
}

type AccessPointState struct {
}

func (AccessPointState) ElementType() reflect.Type {
	return reflect.TypeOf((*accessPointState)(nil)).Elem()
}

type accessPointArgs struct {
	// The name of the bucket that you want to associate this Access Point with.
	Bucket string `pulumi:"bucket"`
	// The Access Point Policy you want to apply to this access point.
	Policy       interface{} `pulumi:"policy"`
	PolicyStatus interface{} `pulumi:"policyStatus"`
	// The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.
	PublicAccessBlockConfiguration *AccessPointPublicAccessBlockConfiguration `pulumi:"publicAccessBlockConfiguration"`
	// If you include this field, Amazon S3 restricts access to this Access Point to requests from the specified Virtual Private Cloud (VPC).
	VpcConfiguration *AccessPointVpcConfiguration `pulumi:"vpcConfiguration"`
}

// The set of arguments for constructing a AccessPoint resource.
type AccessPointArgs struct {
	// The name of the bucket that you want to associate this Access Point with.
	Bucket pulumi.StringInput
	// The Access Point Policy you want to apply to this access point.
	Policy       pulumi.Input
	PolicyStatus pulumi.Input
	// The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.
	PublicAccessBlockConfiguration AccessPointPublicAccessBlockConfigurationPtrInput
	// If you include this field, Amazon S3 restricts access to this Access Point to requests from the specified Virtual Private Cloud (VPC).
	VpcConfiguration AccessPointVpcConfigurationPtrInput
}

func (AccessPointArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*accessPointArgs)(nil)).Elem()
}

type AccessPointInput interface {
	pulumi.Input

	ToAccessPointOutput() AccessPointOutput
	ToAccessPointOutputWithContext(ctx context.Context) AccessPointOutput
}

func (*AccessPoint) ElementType() reflect.Type {
	return reflect.TypeOf((*AccessPoint)(nil))
}

func (i *AccessPoint) ToAccessPointOutput() AccessPointOutput {
	return i.ToAccessPointOutputWithContext(context.Background())
}

func (i *AccessPoint) ToAccessPointOutputWithContext(ctx context.Context) AccessPointOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccessPointOutput)
}

type AccessPointOutput struct{ *pulumi.OutputState }

func (AccessPointOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AccessPoint)(nil))
}

func (o AccessPointOutput) ToAccessPointOutput() AccessPointOutput {
	return o
}

func (o AccessPointOutput) ToAccessPointOutputWithContext(ctx context.Context) AccessPointOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(AccessPointOutput{})
}
