// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SNS::Topic
 */
export function getTopic(args: GetTopicArgs, opts?: pulumi.InvokeOptions): Promise<GetTopicResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:sns:getTopic", {
        "topicArn": args.topicArn,
    }, opts);
}

export interface GetTopicArgs {
    topicArn: string;
}

export interface GetTopicResult {
    /**
     * The archive policy determines the number of days Amazon SNS retains messages. You can set a retention period from 1 to 365 days.
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SNS::Topic` for more information about the expected schema for this property.
     */
    readonly archivePolicy?: any;
    /**
     * Enables content-based deduplication for FIFO topics. By default, ContentBasedDeduplication is set to false. If you create a FIFO topic and this attribute is false, you must specify a value for the MessageDeduplicationId parameter for the Publish action.
     *
     * When you set ContentBasedDeduplication to true, Amazon SNS uses a SHA-256 hash to generate the MessageDeduplicationId using the body of the message (but not the attributes of the message).
     *
     * (Optional) To override the generated value, you can specify a value for the the MessageDeduplicationId parameter for the Publish action.
     */
    readonly contentBasedDeduplication?: boolean;
    /**
     * The body of the policy document you want to use for this topic.
     *
     * You can only add one policy per topic.
     *
     * The policy must be in JSON string format.
     *
     * Length Constraints: Maximum length of 30720
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SNS::Topic` for more information about the expected schema for this property.
     */
    readonly dataProtectionPolicy?: any;
    /**
     * Delivery status logging configuration for supported protocols for an Amazon SNS topic.
     */
    readonly deliveryStatusLogging?: outputs.sns.TopicLoggingConfig[];
    /**
     * The display name to use for an Amazon SNS topic with SMS subscriptions.
     */
    readonly displayName?: string;
    /**
     * The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see Key Terms. For more examples, see KeyId in the AWS Key Management Service API Reference.
     *
     * This property applies only to [server-side-encryption](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html).
     */
    readonly kmsMasterKeyId?: string;
    /**
     * Version of the Amazon SNS signature used. If the SignatureVersion is 1, Signature is a Base64-encoded SHA1withRSA signature of the Message, MessageId, Type, Timestamp, and TopicArn values. If the SignatureVersion is 2, Signature is a Base64-encoded SHA256withRSA signature of the Message, MessageId, Type, Timestamp, and TopicArn values.
     */
    readonly signatureVersion?: string;
    /**
     * The SNS subscriptions (endpoints) for this topic.
     */
    readonly subscription?: outputs.sns.TopicSubscription[];
    readonly tags?: outputs.sns.TopicTag[];
    readonly topicArn?: string;
    /**
     * Tracing mode of an Amazon SNS topic. By default TracingConfig is set to PassThrough, and the topic passes through the tracing header it receives from an SNS publisher to its subscriptions. If set to Active, SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true. Only supported on standard topics.
     */
    readonly tracingConfig?: string;
}
/**
 * Resource Type definition for AWS::SNS::Topic
 */
export function getTopicOutput(args: GetTopicOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTopicResult> {
    return pulumi.output(args).apply((a: any) => getTopic(a, opts))
}

export interface GetTopicOutputArgs {
    topicArn: pulumi.Input<string>;
}
