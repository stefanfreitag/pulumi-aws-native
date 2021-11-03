// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package datasync

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::DataSync::LocationObjectStorage.
type LocationObjectStorage struct {
	pulumi.CustomResourceState

	// Optional. The access key is used if credentials are required to access the self-managed object storage server.
	AccessKey pulumi.StringPtrOutput `pulumi:"accessKey"`
	// The Amazon Resource Name (ARN) of the agents associated with the self-managed object storage server location.
	AgentArns pulumi.StringArrayOutput `pulumi:"agentArns"`
	// The name of the bucket on the self-managed object storage server.
	BucketName pulumi.StringOutput `pulumi:"bucketName"`
	// The Amazon Resource Name (ARN) of the location that is created.
	LocationArn pulumi.StringOutput `pulumi:"locationArn"`
	// The URL of the object storage location that was described.
	LocationUri pulumi.StringOutput `pulumi:"locationUri"`
	// Optional. The secret key is used if credentials are required to access the self-managed object storage server.
	SecretKey pulumi.StringPtrOutput `pulumi:"secretKey"`
	// The name of the self-managed object storage server. This value is the IP address or Domain Name Service (DNS) name of the object storage server.
	ServerHostname pulumi.StringOutput `pulumi:"serverHostname"`
	// The port that your self-managed server accepts inbound network traffic on.
	ServerPort pulumi.IntPtrOutput `pulumi:"serverPort"`
	// The protocol that the object storage server uses to communicate.
	ServerProtocol LocationObjectStorageServerProtocolPtrOutput `pulumi:"serverProtocol"`
	// The subdirectory in the self-managed object storage server that is used to read data from.
	Subdirectory pulumi.StringPtrOutput `pulumi:"subdirectory"`
	// An array of key-value pairs to apply to this resource.
	Tags LocationObjectStorageTagArrayOutput `pulumi:"tags"`
}

// NewLocationObjectStorage registers a new resource with the given unique name, arguments, and options.
func NewLocationObjectStorage(ctx *pulumi.Context,
	name string, args *LocationObjectStorageArgs, opts ...pulumi.ResourceOption) (*LocationObjectStorage, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AgentArns == nil {
		return nil, errors.New("invalid value for required argument 'AgentArns'")
	}
	if args.BucketName == nil {
		return nil, errors.New("invalid value for required argument 'BucketName'")
	}
	if args.ServerHostname == nil {
		return nil, errors.New("invalid value for required argument 'ServerHostname'")
	}
	var resource LocationObjectStorage
	err := ctx.RegisterResource("aws-native:datasync:LocationObjectStorage", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLocationObjectStorage gets an existing LocationObjectStorage resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLocationObjectStorage(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LocationObjectStorageState, opts ...pulumi.ResourceOption) (*LocationObjectStorage, error) {
	var resource LocationObjectStorage
	err := ctx.ReadResource("aws-native:datasync:LocationObjectStorage", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LocationObjectStorage resources.
type locationObjectStorageState struct {
}

type LocationObjectStorageState struct {
}

func (LocationObjectStorageState) ElementType() reflect.Type {
	return reflect.TypeOf((*locationObjectStorageState)(nil)).Elem()
}

type locationObjectStorageArgs struct {
	// Optional. The access key is used if credentials are required to access the self-managed object storage server.
	AccessKey *string `pulumi:"accessKey"`
	// The Amazon Resource Name (ARN) of the agents associated with the self-managed object storage server location.
	AgentArns []string `pulumi:"agentArns"`
	// The name of the bucket on the self-managed object storage server.
	BucketName string `pulumi:"bucketName"`
	// Optional. The secret key is used if credentials are required to access the self-managed object storage server.
	SecretKey *string `pulumi:"secretKey"`
	// The name of the self-managed object storage server. This value is the IP address or Domain Name Service (DNS) name of the object storage server.
	ServerHostname string `pulumi:"serverHostname"`
	// The port that your self-managed server accepts inbound network traffic on.
	ServerPort *int `pulumi:"serverPort"`
	// The protocol that the object storage server uses to communicate.
	ServerProtocol *LocationObjectStorageServerProtocol `pulumi:"serverProtocol"`
	// The subdirectory in the self-managed object storage server that is used to read data from.
	Subdirectory *string `pulumi:"subdirectory"`
	// An array of key-value pairs to apply to this resource.
	Tags []LocationObjectStorageTag `pulumi:"tags"`
}

// The set of arguments for constructing a LocationObjectStorage resource.
type LocationObjectStorageArgs struct {
	// Optional. The access key is used if credentials are required to access the self-managed object storage server.
	AccessKey pulumi.StringPtrInput
	// The Amazon Resource Name (ARN) of the agents associated with the self-managed object storage server location.
	AgentArns pulumi.StringArrayInput
	// The name of the bucket on the self-managed object storage server.
	BucketName pulumi.StringInput
	// Optional. The secret key is used if credentials are required to access the self-managed object storage server.
	SecretKey pulumi.StringPtrInput
	// The name of the self-managed object storage server. This value is the IP address or Domain Name Service (DNS) name of the object storage server.
	ServerHostname pulumi.StringInput
	// The port that your self-managed server accepts inbound network traffic on.
	ServerPort pulumi.IntPtrInput
	// The protocol that the object storage server uses to communicate.
	ServerProtocol LocationObjectStorageServerProtocolPtrInput
	// The subdirectory in the self-managed object storage server that is used to read data from.
	Subdirectory pulumi.StringPtrInput
	// An array of key-value pairs to apply to this resource.
	Tags LocationObjectStorageTagArrayInput
}

func (LocationObjectStorageArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*locationObjectStorageArgs)(nil)).Elem()
}

type LocationObjectStorageInput interface {
	pulumi.Input

	ToLocationObjectStorageOutput() LocationObjectStorageOutput
	ToLocationObjectStorageOutputWithContext(ctx context.Context) LocationObjectStorageOutput
}

func (*LocationObjectStorage) ElementType() reflect.Type {
	return reflect.TypeOf((*LocationObjectStorage)(nil))
}

func (i *LocationObjectStorage) ToLocationObjectStorageOutput() LocationObjectStorageOutput {
	return i.ToLocationObjectStorageOutputWithContext(context.Background())
}

func (i *LocationObjectStorage) ToLocationObjectStorageOutputWithContext(ctx context.Context) LocationObjectStorageOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LocationObjectStorageOutput)
}

type LocationObjectStorageOutput struct{ *pulumi.OutputState }

func (LocationObjectStorageOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LocationObjectStorage)(nil))
}

func (o LocationObjectStorageOutput) ToLocationObjectStorageOutput() LocationObjectStorageOutput {
	return o
}

func (o LocationObjectStorageOutput) ToLocationObjectStorageOutputWithContext(ctx context.Context) LocationObjectStorageOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LocationObjectStorageInput)(nil)).Elem(), &LocationObjectStorage{})
	pulumi.RegisterOutputType(LocationObjectStorageOutput{})
}
