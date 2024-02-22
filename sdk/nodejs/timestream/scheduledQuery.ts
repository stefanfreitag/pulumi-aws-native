// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::Timestream::ScheduledQuery resource creates a Timestream Scheduled Query.
 */
export class ScheduledQuery extends pulumi.CustomResource {
    /**
     * Get an existing ScheduledQuery resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ScheduledQuery {
        return new ScheduledQuery(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:timestream:ScheduledQuery';

    /**
     * Returns true if the given object is an instance of ScheduledQuery.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ScheduledQuery {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ScheduledQuery.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly clientToken!: pulumi.Output<string | undefined>;
    public readonly errorReportConfiguration!: pulumi.Output<outputs.timestream.ScheduledQueryErrorReportConfiguration>;
    public readonly kmsKeyId!: pulumi.Output<string | undefined>;
    public readonly notificationConfiguration!: pulumi.Output<outputs.timestream.ScheduledQueryNotificationConfiguration>;
    public readonly queryString!: pulumi.Output<string>;
    public readonly scheduleConfiguration!: pulumi.Output<outputs.timestream.ScheduledQueryScheduleConfiguration>;
    public readonly scheduledQueryExecutionRoleArn!: pulumi.Output<string>;
    public readonly scheduledQueryName!: pulumi.Output<string | undefined>;
    /**
     * Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results.
     */
    public /*out*/ readonly sqErrorReportConfiguration!: pulumi.Output<string>;
    /**
     * The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with alias/. If ErrorReportConfiguration uses SSE_KMS as encryption type, the same KmsKeyId is used to encrypt the error report at rest.
     */
    public /*out*/ readonly sqKmsKeyId!: pulumi.Output<string>;
    /**
     * The name of the scheduled query. Scheduled query names must be unique within each Region.
     */
    public /*out*/ readonly sqName!: pulumi.Output<string>;
    /**
     * Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it.
     */
    public /*out*/ readonly sqNotificationConfiguration!: pulumi.Output<string>;
    /**
     * The query string to run. Parameter names can be specified in the query string @ character followed by an identifier. The named Parameter @scheduled_runtime is reserved and can be used in the query to get the time at which the query is scheduled to run. The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of @scheduled_runtime paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the @scheduled_runtime parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.
     */
    public /*out*/ readonly sqQueryString!: pulumi.Output<string>;
    /**
     * Configuration for when the scheduled query is executed.
     */
    public /*out*/ readonly sqScheduleConfiguration!: pulumi.Output<string>;
    /**
     * The ARN for the IAM role that Timestream will assume when running the scheduled query.
     */
    public /*out*/ readonly sqScheduledQueryExecutionRoleArn!: pulumi.Output<string>;
    /**
     * Configuration of target store where scheduled query results are written to.
     */
    public /*out*/ readonly sqTargetConfiguration!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    public readonly targetConfiguration!: pulumi.Output<outputs.timestream.ScheduledQueryTargetConfiguration | undefined>;

    /**
     * Create a ScheduledQuery resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ScheduledQueryArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.errorReportConfiguration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'errorReportConfiguration'");
            }
            if ((!args || args.notificationConfiguration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'notificationConfiguration'");
            }
            if ((!args || args.queryString === undefined) && !opts.urn) {
                throw new Error("Missing required property 'queryString'");
            }
            if ((!args || args.scheduleConfiguration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'scheduleConfiguration'");
            }
            if ((!args || args.scheduledQueryExecutionRoleArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'scheduledQueryExecutionRoleArn'");
            }
            resourceInputs["clientToken"] = args ? args.clientToken : undefined;
            resourceInputs["errorReportConfiguration"] = args ? args.errorReportConfiguration : undefined;
            resourceInputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            resourceInputs["notificationConfiguration"] = args ? args.notificationConfiguration : undefined;
            resourceInputs["queryString"] = args ? args.queryString : undefined;
            resourceInputs["scheduleConfiguration"] = args ? args.scheduleConfiguration : undefined;
            resourceInputs["scheduledQueryExecutionRoleArn"] = args ? args.scheduledQueryExecutionRoleArn : undefined;
            resourceInputs["scheduledQueryName"] = args ? args.scheduledQueryName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["targetConfiguration"] = args ? args.targetConfiguration : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["sqErrorReportConfiguration"] = undefined /*out*/;
            resourceInputs["sqKmsKeyId"] = undefined /*out*/;
            resourceInputs["sqName"] = undefined /*out*/;
            resourceInputs["sqNotificationConfiguration"] = undefined /*out*/;
            resourceInputs["sqQueryString"] = undefined /*out*/;
            resourceInputs["sqScheduleConfiguration"] = undefined /*out*/;
            resourceInputs["sqScheduledQueryExecutionRoleArn"] = undefined /*out*/;
            resourceInputs["sqTargetConfiguration"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["clientToken"] = undefined /*out*/;
            resourceInputs["errorReportConfiguration"] = undefined /*out*/;
            resourceInputs["kmsKeyId"] = undefined /*out*/;
            resourceInputs["notificationConfiguration"] = undefined /*out*/;
            resourceInputs["queryString"] = undefined /*out*/;
            resourceInputs["scheduleConfiguration"] = undefined /*out*/;
            resourceInputs["scheduledQueryExecutionRoleArn"] = undefined /*out*/;
            resourceInputs["scheduledQueryName"] = undefined /*out*/;
            resourceInputs["sqErrorReportConfiguration"] = undefined /*out*/;
            resourceInputs["sqKmsKeyId"] = undefined /*out*/;
            resourceInputs["sqName"] = undefined /*out*/;
            resourceInputs["sqNotificationConfiguration"] = undefined /*out*/;
            resourceInputs["sqQueryString"] = undefined /*out*/;
            resourceInputs["sqScheduleConfiguration"] = undefined /*out*/;
            resourceInputs["sqScheduledQueryExecutionRoleArn"] = undefined /*out*/;
            resourceInputs["sqTargetConfiguration"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["targetConfiguration"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["clientToken", "errorReportConfiguration", "kmsKeyId", "notificationConfiguration", "queryString", "scheduleConfiguration", "scheduledQueryExecutionRoleArn", "scheduledQueryName", "targetConfiguration"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ScheduledQuery.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ScheduledQuery resource.
 */
export interface ScheduledQueryArgs {
    clientToken?: pulumi.Input<string>;
    errorReportConfiguration: pulumi.Input<inputs.timestream.ScheduledQueryErrorReportConfigurationArgs>;
    kmsKeyId?: pulumi.Input<string>;
    notificationConfiguration: pulumi.Input<inputs.timestream.ScheduledQueryNotificationConfigurationArgs>;
    queryString: pulumi.Input<string>;
    scheduleConfiguration: pulumi.Input<inputs.timestream.ScheduledQueryScheduleConfigurationArgs>;
    scheduledQueryExecutionRoleArn: pulumi.Input<string>;
    scheduledQueryName?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    targetConfiguration?: pulumi.Input<inputs.timestream.ScheduledQueryTargetConfigurationArgs>;
}
