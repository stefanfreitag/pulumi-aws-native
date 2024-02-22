// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package datasync

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::DataSync::LocationHDFS.
func LookupLocationHdfs(ctx *pulumi.Context, args *LookupLocationHdfsArgs, opts ...pulumi.InvokeOption) (*LookupLocationHdfsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupLocationHdfsResult
	err := ctx.Invoke("aws-native:datasync:getLocationHdfs", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupLocationHdfsArgs struct {
	// The Amazon Resource Name (ARN) of the HDFS location.
	LocationArn string `pulumi:"locationArn"`
}

type LookupLocationHdfsResult struct {
	// ARN(s) of the agent(s) to use for an HDFS location.
	AgentArns []string `pulumi:"agentArns"`
	// The authentication mode used to determine identity of user.
	AuthenticationType *LocationHdfsAuthenticationType `pulumi:"authenticationType"`
	// Size of chunks (blocks) in bytes that the data is divided into when stored in the HDFS cluster.
	BlockSize *int `pulumi:"blockSize"`
	// The unique identity, or principal, to which Kerberos can assign tickets.
	KerberosPrincipal *string `pulumi:"kerberosPrincipal"`
	// The identifier for the Key Management Server where the encryption keys that encrypt data inside HDFS clusters are stored.
	KmsKeyProviderUri *string `pulumi:"kmsKeyProviderUri"`
	// The Amazon Resource Name (ARN) of the HDFS location.
	LocationArn *string `pulumi:"locationArn"`
	// The URL of the HDFS location that was described.
	LocationUri *string `pulumi:"locationUri"`
	// An array of Name Node(s) of the HDFS location.
	NameNodes        []LocationHdfsNameNode        `pulumi:"nameNodes"`
	QopConfiguration *LocationHdfsQopConfiguration `pulumi:"qopConfiguration"`
	// Number of copies of each block that exists inside the HDFS cluster.
	ReplicationFactor *int `pulumi:"replicationFactor"`
	// The user name that has read and write permissions on the specified HDFS cluster.
	SimpleUser *string `pulumi:"simpleUser"`
	// An array of key-value pairs to apply to this resource.
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupLocationHdfsOutput(ctx *pulumi.Context, args LookupLocationHdfsOutputArgs, opts ...pulumi.InvokeOption) LookupLocationHdfsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLocationHdfsResult, error) {
			args := v.(LookupLocationHdfsArgs)
			r, err := LookupLocationHdfs(ctx, &args, opts...)
			var s LookupLocationHdfsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupLocationHdfsResultOutput)
}

type LookupLocationHdfsOutputArgs struct {
	// The Amazon Resource Name (ARN) of the HDFS location.
	LocationArn pulumi.StringInput `pulumi:"locationArn"`
}

func (LookupLocationHdfsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLocationHdfsArgs)(nil)).Elem()
}

type LookupLocationHdfsResultOutput struct{ *pulumi.OutputState }

func (LookupLocationHdfsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLocationHdfsResult)(nil)).Elem()
}

func (o LookupLocationHdfsResultOutput) ToLookupLocationHdfsResultOutput() LookupLocationHdfsResultOutput {
	return o
}

func (o LookupLocationHdfsResultOutput) ToLookupLocationHdfsResultOutputWithContext(ctx context.Context) LookupLocationHdfsResultOutput {
	return o
}

// ARN(s) of the agent(s) to use for an HDFS location.
func (o LookupLocationHdfsResultOutput) AgentArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupLocationHdfsResult) []string { return v.AgentArns }).(pulumi.StringArrayOutput)
}

// The authentication mode used to determine identity of user.
func (o LookupLocationHdfsResultOutput) AuthenticationType() LocationHdfsAuthenticationTypePtrOutput {
	return o.ApplyT(func(v LookupLocationHdfsResult) *LocationHdfsAuthenticationType { return v.AuthenticationType }).(LocationHdfsAuthenticationTypePtrOutput)
}

// Size of chunks (blocks) in bytes that the data is divided into when stored in the HDFS cluster.
func (o LookupLocationHdfsResultOutput) BlockSize() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupLocationHdfsResult) *int { return v.BlockSize }).(pulumi.IntPtrOutput)
}

// The unique identity, or principal, to which Kerberos can assign tickets.
func (o LookupLocationHdfsResultOutput) KerberosPrincipal() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLocationHdfsResult) *string { return v.KerberosPrincipal }).(pulumi.StringPtrOutput)
}

// The identifier for the Key Management Server where the encryption keys that encrypt data inside HDFS clusters are stored.
func (o LookupLocationHdfsResultOutput) KmsKeyProviderUri() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLocationHdfsResult) *string { return v.KmsKeyProviderUri }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Name (ARN) of the HDFS location.
func (o LookupLocationHdfsResultOutput) LocationArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLocationHdfsResult) *string { return v.LocationArn }).(pulumi.StringPtrOutput)
}

// The URL of the HDFS location that was described.
func (o LookupLocationHdfsResultOutput) LocationUri() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLocationHdfsResult) *string { return v.LocationUri }).(pulumi.StringPtrOutput)
}

// An array of Name Node(s) of the HDFS location.
func (o LookupLocationHdfsResultOutput) NameNodes() LocationHdfsNameNodeArrayOutput {
	return o.ApplyT(func(v LookupLocationHdfsResult) []LocationHdfsNameNode { return v.NameNodes }).(LocationHdfsNameNodeArrayOutput)
}

func (o LookupLocationHdfsResultOutput) QopConfiguration() LocationHdfsQopConfigurationPtrOutput {
	return o.ApplyT(func(v LookupLocationHdfsResult) *LocationHdfsQopConfiguration { return v.QopConfiguration }).(LocationHdfsQopConfigurationPtrOutput)
}

// Number of copies of each block that exists inside the HDFS cluster.
func (o LookupLocationHdfsResultOutput) ReplicationFactor() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupLocationHdfsResult) *int { return v.ReplicationFactor }).(pulumi.IntPtrOutput)
}

// The user name that has read and write permissions on the specified HDFS cluster.
func (o LookupLocationHdfsResultOutput) SimpleUser() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLocationHdfsResult) *string { return v.SimpleUser }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupLocationHdfsResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupLocationHdfsResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLocationHdfsResultOutput{})
}
